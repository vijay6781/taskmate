from django.shortcuts import render,redirect
from .forms import CustumRegisterForm
from django.contrib import messages


def register(request):
    if request.method=="POST":
        register_form = CustumRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New Account Created ,Login to Get Started"))
            return redirect('register')
    else:
        register_form = CustumRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})