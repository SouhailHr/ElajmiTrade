from django.shortcuts import render


# Create your views here.

def presentationview(request):
    """A view that displays the presentation page"""

    return render(request, "presentation/presentation.html")
