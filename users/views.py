from django.shortcuts import render
from django.contrib.auth import logout
# Create your views here.
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request,'registration/logged_out.html')  