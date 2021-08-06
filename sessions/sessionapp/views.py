from django.shortcuts import render, HttpResponse

# Create your views here.
def setsession(request):
    request.session['name'] = 'Sonam'
    request.session.set_expiry(600)
    return render(request, 'setsession.html')

def getsession(request):
    name = request.session['name']
    # name = request.session.get('name', default = 'Guest')
    # keys = request.session.keys()
    # key = request.session.items()
    # age = request.session.setdefault('age', '36')
    request.session.modified = True
    context = {'name': name}
    return render(request, 'getsession.html',context )


def delsession(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'delsession.html')

