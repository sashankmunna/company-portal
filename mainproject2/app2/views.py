from django.shortcuts import render,redirect
from app2.models import Employee,News,Calendar
from app2.forms import EmpForm,NewsForm,CalendarForm,SignupForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
	return render(request,'app2/home.html')

@login_required
def HR(request):
	return render(request,'app2/HR.html')

def employee(request):
	return render(request,'app2/employee.html')

def emptable(request):
	emp = Employee.objects.all()
	return render(request,'app2/emptable.html',{"e":emp})

def viewemp(request):
	emp = Employee.objects.all()
	return render(request,'app2/viewemp.html',{"e":emp})

def empform_view(request):
	form = EmpForm()
	if request.method == "POST":
		form = EmpForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/emptable')
	return render(request,'app2/empform.html',{'form':form})

def delete_view(request,id):
	emp = Employee.objects.get(id=id)
	emp.delete()
	return redirect('/emptable')

def update_view(request,id):
	emp = Employee.objects.get(id=id)
	if request.method=="POST":
		form = EmpForm(request.POST,instance=emp)
		if form.is_valid():
			form.save()
			return redirect('/emptable')
	return render(request,'app2/update.html',{'em':emp})

def newsform_view(request):
	news = NewsForm()
	if request.method=="POST":
		form = NewsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/mainnews')
	return render(request,'app2/news.html',{"n":news})

def mainnews_view(request):
	news = News.objects.all()
	return render(request,'app2/mainnews.html',{"news":news})

def viewnews(request):
	news = News.objects.all()
	return render(request,'app2/viewnews.html',{"ne":news})

def calendarform_view(request):
	calendar = CalendarForm()
	if request.method=="POST":
		form = CalendarForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/vct')
	return render(request,'app2/calform.html',{"cal":calendar})

def viewcalendar(request):
	calendar = Calendar.objects.all()
	return render(request,'app2/viewcal.html',{"ca":calendar})

def caltable(request):
	viewcal = Calendar.objects.all()
	return render(request,'app2/caltable.html',{"vct":viewcal})

def logout(request):
	return render(request,'app2/logout.html')

def signup(request):
	form = SignupForm()
	if request.method=="POST":
		form = SignupForm(request.POST)
		user = form.save()
		user.set_password(user.password)
		user.save()
		return HttpResponseRedirect('/accounts/login')
	return render(request,'app2/signup.html',{"form":form})

