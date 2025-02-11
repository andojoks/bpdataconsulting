from django.shortcuts import render, redirect, get_object_or_404
from .models import Service
from django.contrib import messages
from django.http import HttpResponseNotAllowed
from .forms import ContactForm
from .utils import restore_form_from_session

def index(request):
    """
    Simple view to render the homepage (index.html).
    This view is not protected, so anyone can see it.
    """

    # helper function to get session data to rebuild form 
    form, open_modal = restore_form_from_session(request.session, ContactForm)
    
    services = Service.objects.all()
    
    return render(request, 'index.html', {
        'form': form,
        'open_modal': open_modal,
        'services' : services
    })

def services(request):
    """
    Protected view that lists all services (service.html).
    If you want this accessible to everyone (no login needed), 
    remove the @login_required decorator.
    """

    # helper function to get session data to rebuild form 
    form, open_modal = restore_form_from_session(request.session, ContactForm)

    services = Service.objects.all()

    return render(request, 'services.html', {
        'form': form,
        'open_modal': open_modal,
        'services' : services
    })

def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    services = Service.objects.all()

    return render(request, 'service_details.html', {
        'service': service,
        'services' : services
    })

def about(request):
    form, open_modal = restore_form_from_session(request.session, ContactForm)
    
    services = Service.objects.all()

    return render(request, 'about.html', {
        'form': form,
        'open_modal': open_modal,
        'services' : services,
        'limited_services' : services[:3]    # Slice the first 3 services
    })


def contact_us(request):
    form, open_modal = restore_form_from_session(request.session, ContactForm)
    
    services = Service.objects.all()

    return render(request, 'contact_us.html', {
        'form': form,
        'open_modal': open_modal,
        'services' : services,
        'limited_services' : services[:3]    # Slice the first 3 services
    })

def create_contact(request):
    """
    Processes the POST request from the modal contact form.
    If valid, saves to the database and redirects back (or shows a success message).
    If invalid, re-renders the index page with errors so the modal can stay open.
    """
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        next_url = request.POST.get('next', 'index')  # fallback to 'index'
        
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.save()  # Save the form data, including  setting contact_date automatically (per our form)

            messages.success(request, "Thank you! Your message has been sent.")

            return redirect(next_url)
        else:
            # Convert the form data to a dict and store in session.
            #  We can't store the entire form object, so we store just the raw data.
            request.session['contact_form_data'] = request.POST.dict()

            # Convert form errors to JSON so we can restore them later.
            # 'form.errors.as_json()' returns a JSON-serializable dict of errors.
            request.session['contact_form_errors'] = form.errors.as_json()

            # Redirect back to the page
            return redirect(next_url)
            
    else:
       # If it's not a POST, return a 405
       return HttpResponseNotAllowed(['POST'])
    

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)