from django.shortcuts import render_to_response
from django.template import RequestContext
from testflavors import forms
from localflavor.fr.fr_department import DEPARTMENT_CHOICES_PER_REGION

import json
from django.http import HttpResponse

# Create your views here.
def home(request):
    form = forms.MyFlavorForm(request.POST or None)
    return render_to_response('testflavors/home.html',{
        'form': form,
        }, context_instance=RequestContext(request))

def get_departements(request, region):
    departements = [{'optionValue': dept[0], 'optionDisplay': "%s - %s" % (dept[0], dept[1])} for dept in DEPARTMENT_CHOICES_PER_REGION if dept[2] == region]
    return HttpResponse(json.dumps(departements), content_type = "application/json")
