from django.urls import path

from core.views import SignupView, LoginView, ProfileView, UpdatePasswordView

urlpatterns = [
    path("signup", SignupView.as_view(), name="sign up"),
    path("login", LoginView.as_view(), name="login"),
    path("profile", ProfileView.as_view(), name="retrieve-update-destroy user"),
    path("update_password", UpdatePasswordView.as_view(), name="update password")
]
