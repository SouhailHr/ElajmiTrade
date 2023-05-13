from django.shortcuts import render


# Create your views here.

def serviceview(request):
    """A view that displays the home page"""

    return render(request, "services/services.html")
