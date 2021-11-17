from django.shortcuts import render

# Create your views here.
def index(request):
    # get post may on interview
    return render(request, 'MainApp/index.html')