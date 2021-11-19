from django.shortcuts import render, redirect
from django import forms
from django.urls import path
from .short_link import short_link
# from django.db import connection
from django.forms import ModelForm
from .models import Link
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User

class LinkForm (ModelForm):
	class Meta:
		model = Link
		fields = ['Url',]
		labels = {
		'Url':'',
		}

def search_link(request,key):
	filter_link = Link.objects.filter(Url_key = key)
	if filter_link:
		filter_link[0].redirect_count = getattr(filter_link[0],'redirect_count')+1
		filter_link[0].save()
		print(Link.objects.get(Url_key = key).user.date_joined)
		return redirect(getattr(filter_link[0],'Url'))
	else:
		return redirect('/')


def index(request):
	if request.user.is_authenticated:
		if request.method == 'GET':
			form = LinkForm()
			output_index = {'form':form,}
		elif request.method == 'POST':
			form = LinkForm(request.POST)
			if form.is_valid():
				link = form.cleaned_data['Url']
				filter_link = Link.objects.filter(Url = link)
				if filter_link:
					output_key = getattr(filter_link[0],'Url_key')
				else:
					key = short_link(link)
					if key:
		 				output_key = key		
		 				Link(Url = link, Url_key = key, user = request.user, redirect_count = 0).save()
					else:
		 				output_key = False
				form = LinkForm()
				output_index = {'form':form, 'key': output_key, 'link':link,}
		return render(request, 'index.html', output_index)	
	else:
		form = LinkForm()
		output_index = {'form':form,}
		return render(request, 'index.html', output_index)	


def create_user(request):
	form = UserCreationForm(request.POST or None)
	if form.is_bound and form.is_valid():
	 	user = form.save()
	 	return redirect('/accounts/login/')
	return render(request, 'register.html', {'form':form})


def logout_view(request):
	if request.user.is_authenticated:
		logout()