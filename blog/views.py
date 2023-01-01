from django.http import Http404
from django.shortcuts import redirect, render
from blog.forms import SignForm,Login_form
from blog.models import Blog,Enroll
from django.contrib.auth.views import LoginView,LogoutView
from django.core.paginator import Paginator
from django.views.generic import ListView
# Create your views here.
class Mylogin(LoginView):
    template_name='pages/login.html'
    authentication_form=Login_form

class Mylogout(LogoutView):
   success_url='/login/'


   
    


class Home(ListView):
    model = Blog
    template_name ='pages/home.html'
    ordering=['id']
    paginate_by=3
    paginate_orphans = 1

    def paginate_queryset(self, queryset, page_size ):
        try:
            return super(Home,self).paginate_queryset(queryset, page_size)
        except Http404:
            self.kwargs['page']=1
            return super(Home,self).paginate_queryset(queryset, page_size)

 
   

def detail(request, id):
    blog=Blog.objects.filter(pk=id)
    return render(request,'pages/detail.html',{'blog':blog})

def signup(request):
    if request.method =='POST':
        form=SignForm(request.POST)
        if form.is_valid():
            form.save()
            form=SignForm()
            return redirect('login')
    else:
        form=SignForm()
    return render(request,'pages/signup.html',{'form':form})

# Enroll now-----------------------

def enroll_now(request):
    if request.user.is_authenticated:
        user=request.user
        blog_id=request.GET.get('blog_id')
        course=Blog.objects.get(id=blog_id)
        print(course)
        Enroll(user=user,course=course).save()
        return render(request,'pages/enroll.html')
    else:
        return redirect('login')
