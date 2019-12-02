from django.shortcuts import render

def info_list(request):
    return render(request, 'chess/info_list.html',{})
