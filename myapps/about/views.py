from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'nama': 'Halaman Home',
    }
    return render(request, 'index.html', context)