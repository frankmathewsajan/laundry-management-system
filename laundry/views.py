import json
import re

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone

from .__init__ import _md5, MAX_CLOTH_COUNT
from .models import Laundry


# Create your views here.

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = 'vitap_mh3'
        data = json.loads(request.body)
        password = _md5(data.get('password'))

        user = authenticate(request, username=username, password=password)
        print(user, password, username)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'correct'})
        else:
            return JsonResponse({'status': 'wrong'})
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        return render(request, "laundry/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


@login_required(login_url='login')
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "laundry/index.html", {
        'laundries': Laundry.objects.filter(user=request.user)
    })


def info(request, reg_number):
    reg_number = reg_number.upper().strip()
    laundries = Laundry.objects.filter(reg_number=reg_number).order_by('-date')
    print(laundries, reg_number)
    return render(request, "laundry/info.html", {
        "reg_number": reg_number,
        "laundries": laundries
    })


def delete(request, id):
    if request.method == "POST":
        laundry = Laundry.objects.get(id=id)
        reg = laundry.reg_number
        laundry.delete()
        messages.error(request, f"Deleted laundry {id}.")

        # Get the referring page URL
        referer_url = request.META.get('HTTP_REFERER', None)

        # Check if the referer was from the 'info' page
        if referer_url and f'/info/{reg}' in referer_url:
            return redirect('info', reg)
        else:
            # Otherwise, redirect to 'index'
            return redirect('index')


def toggle(request, id):
    try:
        laundry = Laundry.objects.get(id=id)
        data = json.loads(request.body)
        status = data.get('status', None)

        if status:
            laundry.out = True if status == 'out' else False
            laundry.save()

            return JsonResponse({'success': True, 'status': status})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid status.'}, status=400)

    except Laundry.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Laundry not found.'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


def add(request, reg_number):
    if request.method == "POST":
        count = int(request.POST.get('clothCount', 0))
        reg_number = reg_number.upper()

        # Validate cloth count
        if count is None or count < 0 or count > MAX_CLOTH_COUNT:
            messages.error(request, f"Invalid cloth count. Maximum cloth count is {MAX_CLOTH_COUNT}.")
            return redirect('info', reg_number)

        # Validate registration number
        if not re.match(r'^\d{2}[a-zA-Z]{3}\d{4,5}$', reg_number):
            messages.error(request, "Invalid registration number.")
            return redirect('info', reg_number)

        # Get the current date and the first day of the current month
        today = timezone.now()
        first_day_of_month = today.replace(day=1)

        # Get all submissions for the current month for this user
        monthly_submissions = Laundry.objects.filter(
            reg_number=reg_number,
            date__gte=first_day_of_month  # Submissions from the first day of the month
        )

        # Check if the monthly submission limit has been reached
        if monthly_submissions.count() >= 4:
            messages.error(request, f"Maximum 4 submissions allowed per month for {reg_number}.")
            return redirect('info', reg_number)

        # Create a new laundry entry
        new_laundry = Laundry.objects.create(clothCount=count, reg_number=reg_number, user=request.user)

        # Mark all previous submissions as "out" except the new one
        Laundry.objects.filter(reg_number=reg_number).exclude(id=new_laundry.id).update(out=True)

        messages.success(request, "Laundry added successfully.")
        return redirect('info', reg_number)

    return JsonResponse({'status': 'correct'})
