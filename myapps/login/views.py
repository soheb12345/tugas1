from django.shortcuts import render

# Create your views here.

def login_view(request):
    context = {}
    return render(request, 'login/login_view.html', context)