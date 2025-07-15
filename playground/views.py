from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect
from .models import QuoteRequest
import json
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.
# takes a request and response 
#requesy _> response 
# request handeller 

def say_hello(request):
    #pull data fron db , transform , send email 
    return render(request,'home.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def tips(request):
    return render(request, 'paintTip.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials or no admin access'})

    return render(request, 'login.html')

# ADMIN DASHBOARD VIEW
@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    return render(request, 'admin.html')

def submit_quote(request):
    if request.method == 'POST':
        services = request.POST.getlist('services')
        QuoteRequest.objects.create(
            first_name=request.POST.get('firstName'),
            last_name=request.POST.get('lastName'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            address=request.POST.get('address'),
            property_type=request.POST.get('propertyType'),
            services=', '.join(services),
            project_size=request.POST.get('projectSize'),
            timeline=request.POST.get('timeline'),
            budget=request.POST.get('budget'),
            message=request.POST.get('message')
        )
        return redirect('thankyou')

    return redirect('home')


@login_required
def admin_dashboard(request):
    quotes = QuoteRequest.objects.all().order_by('-submitted_at')

    # Convert QuerySet to list of dicts for use in JS
    quote_data = []
    for q in quotes:
        quote_data.append({
            "id": q.id,
            "firstName": q.first_name,
            "lastName": q.last_name,
            "email": q.email,
            "phone": q.phone,
            "address": q.address,
            "propertyType": q.property_type,
            "services": q.services.split(", "),  # split string to list
            "projectSize": q.project_size,
            "timeline": q.timeline,
            "budget": q.budget,
            "message": q.message,
            "status": "new",  # default status, or you can add this to model later
            "submittedAt": q.submitted_at.isoformat(),  # convert to ISO string
        })

    return render(request, 'admin.html', {
        'quote_json': json.dumps(quote_data, cls=DjangoJSONEncoder)
    })