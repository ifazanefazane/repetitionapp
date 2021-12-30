from django.shortcuts import render,redirect
from .models import Service,Client
from .forms import ClientForm
from django.contrib.auth.models import User, auth

# Create your views here.

def index(request):
    service = Service.objects.all()
    context = {
        'service':service,
         }  
    

   
    
    return render(request, 'index.html',context)

def index2(request):
    if request.method == 'POST':
        f = ClientForm(request.POST)
        cnom = request.POST['nom']
        cemail = request.POST['email']
        cquartier = request.POST['subject']
        cmessage = request.POST['classe']
        
        
        cmessage = request.POST['message']

        user = User.objects.create_user(username=cnom,email=cemail,first_name=cquartier,last_name=cmessage)  
        user.save()
        if f.is_valid():
            try:
                f.save()
                return redirect('/')
            except:
                pass
        else:
            f = ClientForm()         
        
    
    return render(request, 'index.html', {'f':f})    



def accepter(request):
    return render(request, 'accepter.html')