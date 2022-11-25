from django.shortcuts import render
from .models import contactlist
from .models import contactform

# Create your views here.

def contactus(request):
    if request.method=='POST':
        # if request method is post wee will have to
        # get that request data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # now we have to store all the post data 
        # into one variable and use that model where real 
        # form fields in 
        contactformdata = contactform(name=name,email=email,subject=subject,message=message)
        # where first name is the model field and 
        # second name is the actual data by getting post request

        # now save the post data by using .save()
        contactformdata.save()







    
    
    contactlistdata = contactlist.objects.all()[0]

    context={
        'contactlist':contactlistdata
    }
    return render(request,'contact.html',context)