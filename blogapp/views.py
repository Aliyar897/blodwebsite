from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import SignUp
from .models import WriteToUs

def homePage(request):

    return render(request, 'index.html')

def login(request):
    context = {}
    if request.method == 'POST':
        data =  SignUp.objects.all()
        username= request.POST['email']
        password= request.POST['password']
        for n in data:
            if username == n.user_email:
                print('User Exits')
                context = {
                    'data':data
                }
        return render(request, 'login.html', context)
    return render(request, 'login.html')
    
def writeUs(request):
    if request.method == 'POST':
        post = WriteToUs()
        post.title= request.POST['title']
        post.author= request.POST['author']
        post.artile= request.POST['article']

        post.save()
  
    return render(request, 'writeus.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def articles(request):
    articles =  WriteToUs.objects.all()

    context ={
        'articles':articles,
    }

    return render(request, 'articles.html', context)

def signUp(request):
    if request.method == 'POST':
        post = SignUp()
        post.user_email= request.POST['useremail']
        post.password= request.POST['userpassword']
        post.save()
        print('Hello world', post)
        return HttpResponseRedirect('login')
        # return render(request, 'login.html')

    return render(request, 'signup.html')

# Create your views here.
