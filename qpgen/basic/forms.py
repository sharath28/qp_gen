from django import forms

class MainForm(forms.Form):
	university       = forms.CharField(label="University",max_length=10,required=False)
	semester         = forms.IntegerField(label="Semester",required=True)
	subject	         = forms.CharField(label="Subject",max_length=50,required=True)
	max_marks        = forms.IntegerField(label="Max Marks",required=True)
	no_of_questions  = forms.IntegerField(label="Number of questions",required=True)
	sub_questions 	 = forms.IntegerField(label="Sub Questions", required=True)


class LoginForm(forms.Form):
	username 	= forms.CharField(label="Username",max_length=50,required=True)
	password	= forms.CharField(label="Password",max_length=50,required=True,widget=forms.PasswordInput)
