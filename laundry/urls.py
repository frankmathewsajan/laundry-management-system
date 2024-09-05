from django.contrib import admin
from django.urls import path, include

from laundry import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("info/<str:reg_number>", views.info, name="info"),
    path("add/<str:reg_number>", views.add, name="add"),
    path("delete/<int:id>", views.delete, name="delete")
]
