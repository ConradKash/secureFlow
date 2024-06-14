# feedback/views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Construct the email message
            subject = 'Feedback Submission'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [settings.DEFAULT_TO_EMAIL]
            message_content = f'Name: {name}\nEmail: {email}\nMessage:\n{message}'
            
            # Send the email
            send_mail(subject, message_content, from_email, to_email, fail_silently=False)
            
            # Redirect to a success page
            return redirect('feedback_success')  # Ensure you have a URL pattern named 'feedback_success'
    else:
        form = FeedbackForm()
    
    return render(request, 'contactus.html', {'form': form})
