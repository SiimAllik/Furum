from django.shortcuts import render, get_object_or_404

def HomeView(request):
    return render(request, "furumapp/index.html")

