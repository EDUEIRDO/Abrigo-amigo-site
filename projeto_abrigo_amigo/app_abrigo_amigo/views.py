from django.shortcuts import render

# Create your views here.
def banco(request):
    return render(request, 'admin/db.html')
