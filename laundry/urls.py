from django.urls import path

from laundry import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("change_password/", views.change_password_view, name="change_password"),
    path("logout/", views.logout_view, name="logout"),
    path("info/<str:reg_number>", views.info, name="info"),
    path("add/<str:reg_number>", views.add, name="add"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("toggle/<int:id>", views.toggle, name="toggle"),

]
