from django.shortcuts import render, render_to_response, RequestContext
from .forms import SignUpForms

def home(request):
    form = SignUpForms(request.POST or None)
    if form.is_valid():
        save_form = form.save(commit=False)
        save_form.save()
    return render_to_response('signups/home.html',locals(), context_instance=RequestContext(request))
