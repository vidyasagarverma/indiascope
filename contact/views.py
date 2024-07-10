from django.shortcuts import render
from .forms import ContactForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

def home(request):

    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            email=form.cleaned_data["email"]
            message=form.cleaned_data["message"]

            Form.objects.create(name=name,email=email,message=message)

            message_body=f" thank your enquiry {name} \n {message}"
            email_message=EmailMessage("Thank you for your request",message_body,to=[email])
            email_message.send()

            messages.success(request,"Form submitted successfully")
    return render(request,"home.html")

