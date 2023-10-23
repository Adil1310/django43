"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp.views import SignUpWithVerification, VerifyEmailView, VerificationSuccessView, VerificationErrorView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SignUpWithVerification.as_view(), name='home'),
    path('verify/<int:user_pk>/<str:token>/', VerifyEmailView.as_view(), name='verify_email'),
    path('verification_success/', VerificationSuccessView.as_view(), name='verification_success'),
    path('verification_error/', VerificationErrorView.as_view(), name='verification_error'),
]
