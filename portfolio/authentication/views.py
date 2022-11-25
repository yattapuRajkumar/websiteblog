from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def authlogin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        # we create a user variable to store
        # requested logging  data
        # we can validate that data with authenticate mehod
        # first username and passwords are from admin default Users table fileds
        # the second ones are from above requested data 

        user = authenticate(request,username=username , password=password)

        # what if a user is validated
        if user is not None:
            # allow him to log in 
            # and redirect to some page when logged in
            login(request,user)
           
            return redirect('profile') # this is path url name ='profile'
        
        else:
            # here error is a one of the message tag
            messages.error(request,'email or password invalid!')




    return render(request,'authentication/login.html')


def authlogout(request):
    # this is django built in logout method
    # when a user logged out 
    # we provide redirect to the login page 
    # by providing login url path name
    logout(request)
    messages.success(request,'successfully logged out')
    return redirect('login')





def authregistration(request):
    if request.method == 'POST':
        name = request.POST['name']
        # name = request.POST.get('name')
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # here we have to write condition 
        # what if password and confirm_password did not match

        if password == confirm_password:
            # if passswords are matched we have to check
            # wether a user or email  already existed or not
            # to check we have to import default django User model
            if User.objects.filter(username=name).exists():
                messages.error(request,'user is already existed')
            
            elif User.objects.filter(email=email).exists():
                messages.error(request,'email is already existed')

                # if user and mail is not there in database
                # create it that user by using default 'create_user'method
            else:
                user = User.objects.create_user(username=name,email=email,password=password)
                user.save()
                # whenever user is registered user is redirected to somewhere
                return redirect('login')


            

        else:
            messages.error(request,'password and conifrm_password did not match')



    return render(request,'authentication/registration.html')






def forgetpassword(request):
    return render(request,'authentication/forget.html')