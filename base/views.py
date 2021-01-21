from django.shortcuts import render,redirect
from .forms import ContactForm



def home(request):
    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('HomePage')
    else:
        f = ContactForm()
    return render(request, 'base/index.html', {'form': f})

