from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name="home"),

    path('products/', views.products, name="products"),
    # path('customer/<str:pk>/', views.customer, name="customer"),
    path('create_transfer/', views.createTransfer, name="create_transfer"),
    path('confirm_transfer/', views.confirmTransfer, name="confirm_transfer"),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # Django save procedure uisb and token
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]
