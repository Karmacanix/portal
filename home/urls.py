from django.contrib.auth import views  as auth_views
from django.urls import path

from home.views import account_settings, signup
from catalogue.views import SidebarListView

urlpatterns = [
    path('', SidebarListView.as_view(), name='show_sidebar'),
    path('account/settings/', account_settings, name='account_settings'),
    path('login/', auth_views.LoginView.as_view(next_page='show_sidebar', template_name="home/login.html"), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name="home/logged_out.html"), name="logout"),
    path(
        "password_change/", auth_views.PasswordChangeView.as_view(template_name="home/change-password.html"), name="password_change"
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(template_name="home/password_change_done.html"),
        name="password_change_done",
    ),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="home/password_reset_form.html"), name="password_reset"),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(template_name="home/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name="home/password_reset_confirm.html"),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(template_name="home/password_reset_complete.html"),
        name="password_reset_complete",
    ),
    path('signup/', signup, name='signup'),
]
