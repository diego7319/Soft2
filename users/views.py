from django.shortcuts import render,  redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from users.forms import Login, Signup




def index(request):
    formaLogin = Login(request.POST or None)
    formaSignup = Signup(request.POST or None)
    context = {
        'formaL': formaLogin,
        'formaS': formaSignup
    }
    return render(request, 'index.html', context)

def login(request):
    pass

def signup(request):
     
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
