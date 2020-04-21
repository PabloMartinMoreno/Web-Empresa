from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Envio de correo y redireccion 
            email = EmailMessage(
                "Frutarian World: Nuevo mensaje de contacto",
                "de {} <{}>\n\nEscribio\n\n{}".format(name,email,content),
                "no-contestar@inbox.mailtrap.io",
                ["pablou90@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                #si todo bien
                return redirect(reverse('contact')+"?ok")
            except: 
                #redireccion a fail
                return redirect(reverse('contact')+"?fail")
            
    return render(request, "contact/contact.html", {'form':contact_form})