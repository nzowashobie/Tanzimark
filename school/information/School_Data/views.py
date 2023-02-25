
# Create your views here.
from django.shortcuts import  render, redirect

from School_Data.models import Students,Infor_school
from .forms import NewUserForm
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
#from django.conf.urls import url
from django.db.models import query
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from School_Data.models import Students
from django.shortcuts import render, redirect
from School_Data.forms import ImageForm
from django.views.generic import TemplateView, ListView
from django.template import loader
from django.db.models import Q
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

class home(ListView):
#def home(request):
    model = Infor_school
    #return render(request, 'home.html')
    template_name = 'home.html'

#from .filters import  Sub_Filter
#def Filt(request):
    #subject = Image.objects.all()
    #myFilter = Sub_Filter(request.GET, queryset=subject)
   # subject = myFilter.qs
    #context = {
       # 'myFilter': myFilter,
       # 'subject': subject,
    #}
   # return render(request, 'search_form.html', context)

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
    
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return render(request, 'search_form.html',{'images':username})
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name='login.html', context={'login_form':form})
#forms
def index(request):
        """Process images uploaded by users"""
        if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                # Get the current instance object to display in the template
                img_obj = form.instance
                return render(request, 'upload.html', {'form': form, 'img_obj': img_obj})
        else:
            form = ImageForm()
        return render(request, 'upload.html', {'form': form})

#sql server search

def display_images(request): 
  
    # getting all the objects of hotel. 
    allimages = Students.objects.all()  
    return render(request, 'index.html',{'images' : allimages})

#search form
def checks(request,check_id): 
  
    # getting all the objects of hotel. 
    check_s = Students.objects.get(name=check_id)
    #check_s = get_object_or_404(Book, id=book_id) 
    print('myoutput',check_s) 
    return render(request, 'check.html',{'images' : check_s})

class search_img(TemplateView):
    template_name = 'search_form.html' 

#get form view

# Create your views here.
class SearchResultsView(ListView):
    model = Students
    template_name = 'search.html'

    def get_queryset(self): # new
        query = self.request.GET.get('s')
        query1 = self.request.GET.get('q')
        query2 = self.request.GET.get('g')
        query3 = self.request.GET.get('p')
        object_list = Students.objects.filter(
            Q(name=query) & Q(Subject=query1) & Q(Grade=query2) & Q(password=query3)
        )
        return object_list

#infor school

def infor(request): 
  
    model = Infor_school
    template_name = 'home.html'



