from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required


def signup(request):
      if request.method == 'POST':
          if (request.POST['password1'] == request.POST['pass']):
              try:
                  user = User.objects.get(username=request.POST['username'])
                  return render(request, 'accounts/signup.html', {'error':'Username Has Already Been Taken'})
              except User.DoesNotExist:
                  if (len(request.POST['pass']) != 0) and (len(request.POST['username']) != 0) and (len(request.POST['email']) != 0):
                      user = User.objects.create_user(request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
                      auth.login(request,user)
                      return redirect('home')
                  else:
                      return render(request, 'accounts/signup.html', {'error':'Please fill up all the fields'})
          else:
                return render(request, 'accounts/signup.html', {'error':'Password Must Match'})
      else:
          return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password1'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',{'error':'Username Or Password Is Incorrect'})
    else:
        return render(request, 'accounts/login.html')

@login_required()
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
        return render(request, 'accounts/signup.html')



@login_required()
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('home')
            messages.success(request, 'Your password was successfully updated!')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })
