from django.shortcuts import render, redirect
from .forms import UserForm

def save_user_name(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # redirect after saving
    else:
        form = UserForm()
    
    return render(request, 'users/user_form.html', {'form': form})

def success(request):
    return render(request, 'users/success.html')
