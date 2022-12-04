from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Створення порожньої форми
        form=UserCreationForm()
    else:
        # Опрацювання заповненої форми
        form=UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user=form.save()
            # Авторизація користувача та редірект на головну сторінку
            login(request,new_user)
            return  redirect('online_notes:index')

    context={'form':form}
    return render(request, 'registration/register.html',context)
