from django.db.models import query
from django.db.models.query_utils import subclasses
from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from home.models import Feedback
from home.models import Contact
from home.models import Booking
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone_number = request.POST.get('phone')
        email = request.POST.get('email')
        query_string = request.POST.get('problem-msg')
        datetime.today

        booking = Booking(name=name, phone_number=phone_number, email=email,
                          query_string=query_string, date=datetime.today())
        booking.save()
        messages.success(
            request, 'Your bookings has been done! We will get to you soon.')

    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')
        datetime.today
        contact = Contact(name=name, email=email, phone=phone,
                          msg=msg, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')

    return render(request, "contact.html")


def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email_address = request.POST.get('email')
        service_taken = request.POST.get('services-taken')
        sub = request.POST.get('subject')
        desc = request.POST.get('msg')
        datetime.today
        feedback = Feedback(name=name, email_address=email_address,
                            service_taken=service_taken, sub=sub, desc=desc, date=datetime.today())
        feedback.save()
        messages.success(request, "Your feedback has been recorded!")

    return render(request, "feedback.html")
