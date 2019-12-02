from django.shortcuts import render
from .models import Info

def info_list(request):
    return render(request, 'chess/info_list.html',{})
