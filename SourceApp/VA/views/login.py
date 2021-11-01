from django.shortcuts import (
    render,
    reverse,
    redirect,
    HttpResponse
)
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from django.contrib.auth.decorators import login_required
from VA.forms import loginForm


def index(request):
    if 'user' in request.session:
        request.session.flush()
        logout(request)
    return redirect(reverse('login'))

def loginPageDisplay(request):
    msg = None
    if 'user' in request.session:
        request.session.flush()
        logout(request)
    if request.method == 'POST':
        form = loginForm.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['user'] = user.firstname
                return redirect(reverse('home'))
            else:
                msg = "invalid username or password"
        else:
            msg = "invalid usename or password"
    else:
        form = loginForm.LoginForm()

    return render(request, 'loginPage.html', context={'form': form, 'msg': msg})

@login_required
def homePageDisplay(request):
    return render(request, 'homePage.html')


def logoutPage(request):
    request.session.flush()
    logout(request)
    return redirect(reverse('login'))
