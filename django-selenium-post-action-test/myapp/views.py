from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProfileForm
from .models import Profile
# Create your views here.
def home(request):
    # return render(request, 'home.html')
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
    
    form = ProfileForm
    profiles = Profile.objects.all()
    return render(request, 'home.html', {'form': form, 'profiles': profiles})