from django.contrib.auth.decorators import login_required
from django.shortcuts import render, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from accounts.forms import PaymentForm, ProfileForm, MyUserForm
from accounts.models import Payment



def login_view(request):
    next_url = request.GET.get('next')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Successful login
            login(request, user)
            redirect_url = next_url if next_url else reverse('ticketing:showtime_list')
            return HttpResponseRedirect(redirect_url)
        else:
            # undefined user or wrong password
            context = {
                'username': username,
                'error': 'کاربری با این مشخصات یافت نشد'
            }
    else:
        context = {}
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))

@login_required
def profile_details(request):
    profile = request.user.profile
    context = {
        'profile': profile
    }
    return render(request, 'accounts/profile_details.html', context)

@login_required
def payment_list(request):
    payments = Payment.objects.filter(profile=request.user.profile).order_by('-transaction_time')
    context = {
        'payment': payments
    }
    return render(request, 'accounts/payment_list.html', context)

@login_required
def payment_creat(request):
    #check if data is correct
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            #create payment
            #commit ro barabar ba False mikonim ta mostaqim dar db save nashe sepas profile ro dasti midim
            payment = payment_form.save(commit=False)
            payment.profile = request.user.profile
            payment.save()
            request.user.profile.deposit(payment.amount)
            return HttpResponseRedirect(reverse('accounts:payment_list'))
    else:
        payment_form = PaymentForm()
    context = {
        'payment_form': payment_form
    }
    return render(request, 'accounts/payment_create.html', context)

@login_required
def profile_edit(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, files=request.FILES,  instance=request.user.profile)
        user_form = MyUserForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return HttpResponseRedirect(reverse('accounts:profile_details'))
    else:
        profile_form = ProfileForm( instance=request.user.profile)
        user_form = MyUserForm(instance=request.user)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request,'accounts/profile_edit.html',context)