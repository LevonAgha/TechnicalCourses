from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>This is my articles page</h1>')



