from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddCustomer
from .models import CustomerRecord
# Create your views here.


def home(request):
    customer_records = CustomerRecord.objects.all()

    if request.method == 'POST':
        # Check if user is logging in with a post method
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.error(
                request, "There was an error logging in, please try again")
            return redirect('home')
    else:
        return render(
            request, 'home.html', {'customer_records': customer_records})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, 'You have successfully Registered! Welcome')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_by_id = CustomerRecord.objects.get(id=pk)
        return render(
            request, 'customer_by_id.html', {'customer_by_id': customer_by_id})
    else:
        messages.error(request, "You must be logged in to view that page...")
        return redirect('home')


def delete_customer(request, pk):
    if request.user.is_authenticated:
        customer_by_id = CustomerRecord.objects.get(id=pk)
        customer_by_id.delete()
        messages.success(request, 'Customer Record deleted sucessfully')
        return redirect('home')
    else:
        messages.error(request, "You must be logged in to view that page...")
        return redirect('home')


def add_customer(request):
    form = AddCustomer(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added...")
                return redirect('home')

        return render(request, 'add_customer.html', {'form': form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')


def update_customer(request, pk):
    if request.user.is_authenticated:
        current_customer = CustomerRecord.objects.get(id=pk)
        form = AddCustomer(request.POST or None, instance=current_customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer details has been Updated")
            return redirect('home')
        return render(request, 'update_customer.html', {'form': form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')
