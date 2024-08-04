"""
    view of the offier app.
"""
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DeclarantForm, EnfantForm, PereForm, MereForm
def Declaration(request):

    return render(request, 'declaration.html')

# def Chef_officier(request):

#     return render(request, 'chef_officier.html')

def Chef_officier(request):
    if request.method == 'POST':
        declarant_form = DeclarantForm(request.POST)
        enfant_form = EnfantForm(request.POST)
        pere_form = PereForm(request.POST)
        mere_form = MereForm(request.POST)
        
        if (declarant_form.is_valid() and 
            enfant_form.is_valid() and 
            pere_form.is_valid() and 
            mere_form.is_valid()):
            
            declarant = declarant_form.save()
            enfant_form.save()
            pere_form.save()
            mere_form.save()
            
            return redirect('success')  # Replace with your actual redirect target
    else:
        declarant_form = DeclarantForm()
        enfant_form = EnfantForm()
        pere_form = PereForm()
        mere_form = MereForm()
        
    context = {
        'declarant_form': declarant_form,
        'enfant_form': enfant_form,
        'pere_form': pere_form,
        'mere_form': mere_form,
    }
    
    return render(request, 'chef_officier.html', context)
