from django.shortcuts import render,redirect
#introduce forms
from django.contrib.auth.forms import UserCreationForm
#import forms
from .forms import CreateUserForm,UserUpdateForm,ProfileUpdateForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')  # Redirect to dashboard after successful registration
        else:
            # Print form errors for debugging
            print(form.errors)
    else:
        form = CreateUserForm()
    
    context = {'form': form}
    return render(request, 'users/register.html', context)



def profile(request):
        return render(request, 'users/profile.html',)

def profile_update(request):
    if request.method=='POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        return redirect('user-profile')
    else:
            user_form = UserUpdateForm(instance=request.user)
            profile_form = ProfileUpdateForm(instance=request.user.profile)



    context={'user_form':user_form, 'profile_form':profile_form}
    return render(request, 'users/profile_update.html',context)
