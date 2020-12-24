from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import *
from .forms import TransferForm, CreateUserForm


def registerPage(request):
    form = CreateUserForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            form = CreateUserForm(request.POST)  # handles all
            if form.is_valid():
                form.save()
                messages.success(request, f"Account for {form.cleaned_data.get('username')} created.")
                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect.')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, 'accounts/dashboard.html')


@login_required(login_url='login')
def products(request):
    transfers = Transfer.objects.all()
    print("tra ", transfers)
    return render(request, 'accounts/products.html', {'transfers': transfers})


@login_required(login_url='login')
def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    transfers = customer.transfer_set.all()
    transfer_count = transfers.count()
    context = {'customer': customer, 'transfers': transfers, 'transfer_count': transfer_count}
    return render(request, 'accounts/customer.html', context)


@login_required(login_url='login')
def createTransfer(request):
    form = TransferForm()
    if request.method == "POST":
        form = TransferForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/transfer_form.html', context)
