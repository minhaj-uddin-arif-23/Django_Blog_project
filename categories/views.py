from django.shortcuts import render,redirect
# Create your views here.
from . import forms
def add_category(request):
    if request.method == 'POST':#user post request korcecah
        category_form = forms.CategoryForm(request.POST)# user ar post request data
        if category_form.is_valid():#post kora data aikane 
            category_form.save()
            return redirect('add_category')
    else:
        category_form = forms.CategoryForm()
    return render(request,'add_category.html',{'form':category_form})