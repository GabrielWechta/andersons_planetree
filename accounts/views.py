from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
    if request.user.is_authenticated:
        username = request.user.username
    transfers = Transfer.objects.all()
    good_transfer = Transfer.objects.none()
    for t in transfers:
        if str(t.customer) == username:
            good_transfer |= Transfer.objects.filter(id=t.id)
    number = good_transfer.count()

    context = {'number': number}
    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
def products(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    transfers = Transfer.objects.all()
    good_transfer = Transfer.objects.none()
    for t in transfers:
        if str(t.customer) == username:
            good_transfer |= Transfer.objects.filter(id=t.id)

    return render(request, 'accounts/products.html', {'transfers': good_transfer})


# @login_required(login_url='login')
# def customer(request, pk):
#     customer = Customer.objects.get(id=pk)
#
#     transfers = customer.transfer_set.all()
#     transfer_count = transfers.count()
#     context = {'customer': customer, 'transfers': transfers, 'transfer_count': transfer_count}
#     return render(request, 'accounts/customer.html', context)


@login_required(login_url='login')
def createTransfer(request):
    form = TransferForm()
    if request.method == "POST":
        user = None
        if request.user.is_authenticated:
            user = request.user
            form = TransferForm(request.POST)
            tmp = form.save(commit=False)
            tmp.customer = user
            # if tmp.is_valid():
            tmp.save()
            context = {'form': form}
            print(form)
            return render(request, 'accounts/transfer_confirm.html', context)

    context = {'form': form}
    return render(request, 'accounts/transfer_form.html', context)


@login_required(login_url='login')
def confirmTransfer(request):
    context = {}
    return render(request, 'accounts/transfer_form.html', context)
