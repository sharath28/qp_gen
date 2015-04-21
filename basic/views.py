from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import MainForm, LoginForm
from .models import SubQuestion, Subject, QuestionPaper, MainQuestion

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

                    return redirect('create_qp')

                else:
                    context['form']         = LoginForm()
                    context['message']      = "Account disabled."
                    context['messageclass'] = "error"

                    return render(request,'login.html',context)
            else:
                context['form']         = LoginForm()
                context['message']      = "Invalid username or password."
                context['messageclass'] = "error"

                return render(request,'login.html',context)


def logout_user(request):
    logout(request)

    return redirect('login')


@login_required(login_url='/')
def create_qp(request):
    context = {}

    if request.method == "GET":
        form = MainForm()
        context['form'] = form

        return render(request,'create.html',context)

    elif request.method == "POST":
        form = MainForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            # university      = data['university']
            semester        = data['semester']
            subject         = data['subject']
            max_marks       = data['max_marks']
            no_of_questions = data['no_of_questions']
            sub_questions   = data['sub_questions']

            
            #To be edited

        return render(request,'view.html',context)


@login_required(login_url='/')
def view_qp(request,qp_id=''):
    context = {}

    if qp_id:
        qp_id = int(qp_id)

        if QuestionPaper.objects.filter(pk=qp_id).exists():
            #Question paper with given id exists

            q = QuestionPaper.objects.get(pk=qp_id)

            #To be edited


        else:
            #Question paper with given id does not exist
           
            context['message']      = "Invalid question paper id."
            context['messageclass'] = "error"

            return render(request,'view.html',context)

    else:
        #No question paper id present in the URL

        context['message']      = "You need to specify a question paper id."
        context['messageclass'] = "error"

        return render(request,'view.html',context)


def contact(request):
    return HttpResponse('Page yet to be created')


def about(request):
    return HttpResponse('Page yet to be created')