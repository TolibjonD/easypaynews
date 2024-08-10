from django.urls import path
from .views import login_view, logout_view, profile, user_register
from django.contrib.auth.views import PasswordChangeDoneView,PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", user_register, name="register"),
    path("logout/", logout_view, name="logout"),
    path("password-change/", PasswordChangeView.as_view(), name="password_change"),
    path("password-change-done/", PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("password-reset/", PasswordResetView.as_view(), name="password_reset"),
    path("password-reset/done/", PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("password-reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("password-reset/complete/", PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("profile/", profile, name="profile"),
]
