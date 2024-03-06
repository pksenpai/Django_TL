from django.shortcuts import render
from django.views import View


def home(request):
    return render(request, 'home.html')

class HomeView(View): # same with the home function
    
    def get(self, request): # same result with home()
        return render(request, 'home.html')

    def post(self, request):
        return 

    def put(self, request):
        return 

    def patch(self, request):
        return 

    def delete(self, request):
        return 

    def head(self, request):
        return 

    def options(self, request):
        return 

    def trace(self, request):
        return 

"""
HTTP_METHODS:
    "get",
    "post",
    "put",
    "patch",
    "delete",
    "head",
    "options",
    "trace",
"""

