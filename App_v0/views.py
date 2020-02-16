from django.shortcuts import render

# Create your views here.

def Start(request):
    return render(request, 'index.html')
