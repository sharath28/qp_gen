from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MainForm,LoginForm
from .models import SubQuestion,Subject,QuestionPaper,MainQuestion
# Create your views here.
def login_user(request):
	context = {}
	if request.method == 'GET':
		if request.user.is_authenticated():
			return redirect('qpdetail')
			
		form = LoginForm()
		context['form'] = form

		return render(request,'login.html',context)

	elif request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			data = form.cleaned_data

			username = data['username']
			password = data['password']

			user = authenticate(username=username, password=password)

			if user is not None:
				if user.is_active:
					login(request, user)

					return redirect('qpdetail')

				else:
					context['form']			= LoginForm()
					context['message']		= "Account disabled."
					context['messageclass']	= "error"

					return render(request,'login.html',context)
			else:
				context['form']			= LoginForm()
				context['message']		= "Invalid username or password."
				context['messageclass']	= "error"

				return render(request,'login.html',context)

@login_required(login_url='/')
def qpdetail(request):
	context = {}

	if request.method == "GET":

		form = MainForm()
		context['form']			= form
		context['form_type']	= 1

		return render(request,'qpdetail.html',context)

	elif request.method == "POST":

		form = MainForm(request.POST)

		if form.is_valid():
			data = form.cleaned_data

			university      = str(data['university'])
			semester	    = data['semester']
			subject	        = str(data['subject'])
			max_marks	    = data['max_marks']
			no_of_questions	= data['no_of_questions']
			sub_questions	= data['sub_questions']

		context['form']		= form	
		return render(request,'qpdetail.html',context)

def logout_user(request):
	logout(request)

	return redirect('login')

def contact(request):
	return HttpResponse('Page yet to be created')

def about(request):
	return HttpResponse('Page yet to be created')





			
	

