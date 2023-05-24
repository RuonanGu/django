
# Create your views here.
from django.http import HttpResponse

def index(resquest):
    line1 = '<h1 style="text-align: center">my first webpage!!!</h1>'
    return HttpResponse(line1)
