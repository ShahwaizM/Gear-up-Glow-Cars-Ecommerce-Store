from django.shortcuts import render
from django.http import HttpResponseRedirect
from store.models.contact import ContactMessage

def contact_page(request):
    error_message = None  
    if request.method == 'POST':
        first_name = request.POST.get('firstName', '').strip()
        last_name = request.POST.get('lastName', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if not (first_name and last_name and email and subject and message):
            print("Form data is missing")
            error_message = "All fields are required."
        else:
            print("Form  is missing")
            from django.core.validators import validate_email
            from django.core.exceptions import ValidationError
            try:
                validate_email(email)
            except ValidationError:
                error_message = "Invalid email format."
            else:
                new_message = ContactMessage(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    subject=subject,
                    message=message
                )
                new_message.save()
                return HttpResponseRedirect('/contact/')  

    return render(request, 'contact.html', {'error_message': error_message})
