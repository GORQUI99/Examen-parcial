from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required



def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect(reverse('login'))


