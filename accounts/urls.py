from django.urls import path, include ,reverse_lazy, re_path
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView

urlpatterns = [

    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('change_password', views.change_password, name='change_password'),
    path('password-reset/', PasswordResetView.as_view(success_url=reverse_lazy('password_reset_done')) , name= 'password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view() , name ='password_reset_done' ),
    re_path(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(success_url=reverse_lazy('password_reset_complete')),name='password_reset_confirm'),
    path('password-reset/complete/',PasswordResetCompleteView.as_view() , name='password_reset_complete'),
]
