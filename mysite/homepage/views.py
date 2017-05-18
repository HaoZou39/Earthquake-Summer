from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.template import Context,loader,RequestContext
from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse, Http404,HttpResponseRedirect,HttpResponseNotFound
import os # Library used to read files in one folder
from homepage.models import posts

def homepage(request):
	filenames = next(os.walk('static\images'))[2]# Acquire filenames for all files under a certain folder
	return render(request,'index.html',{'filenames':filenames})