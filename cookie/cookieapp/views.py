from django.shortcuts import render, HttpResponse
from datetime import datetime,timedelta

# Create your views here.
def index(request):
    return HttpResponse('this set is setcookie testing')

def setcookie(request):
    response = render(request, 'setcookie.html')

    response.set_signed_cookie('name', 'murali',salt='nm', expires=datetime.utcnow()+timedelta(days=2))
    return response

def getcookie(request):

    name = request.get_signed_cookie('name', default = 'Guest',salt = 'nm')

    return render(request, 'getcookie.html', {'name':name})

def delcookie(request):
    response = render(request, 'delcookie.html')
    response.delete_cookie('name')
    return response