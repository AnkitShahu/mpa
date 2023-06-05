from django.shortcuts import render
from .models import Home, Doctor, Contact

# Create your views here.
def home(request):
    context = {"context_variable": " hello", }
    books = Home.objects.all()
    doc = Doctor.objects.all()
    context = {"book": books, "doc": doc }
    print(books)
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")


def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        office_location = request.POST.get('office_location')
        doctor = request.POST.get('doctor')

        contact = Contact(
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            message=message,
            office_location=office_location,
            doctor=doctor
        )
        print(contact)
        contact.save()
        
        # Handle successful form submission (e.g., redirect)
        # return redirect('success')
    
    return render(request, 'contact.html')
