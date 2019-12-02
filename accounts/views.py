from django.shortcuts import render ,redirect,HttpResponseRedirect
from .forms import LoginForm ,registerForm
from django.contrib.auth import authenticate, login, logout
from django.http import request
# Create your views here.



def login_view(request):
    form=LoginForm(request.POST or None)
    
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect('../../index')

    content={
        'form':form,
        'title' : "Giriş Yap"
    }
    return render(request, 'accounts/loginforms.html',content)



def register_view(request):
    form=registerForm(request.POST or None)

    if form.is_valid():
        user=form.save(commit=False)
        password=form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user=authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("../../index")

    content={
        'form' : form,
        'title' : 'Üye Ol'
    }
    
    return render(request, 'accounts/loginforms.html' , content)


def logout_view(request):
    logout(request)
    return redirect("../../index")