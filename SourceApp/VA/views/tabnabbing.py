from django.shortcuts import(
    render,
    redirect,
    reverse
)

from django.contrib.auth.decorators import login_required

@login_required
def tabnabbingPage(request):
    return render(request, 'tabnabbingPage.html')

@login_required
def tabnabbingFixedPage(request):
    return render(request, 'tabnabbing-fixedPage.html')
