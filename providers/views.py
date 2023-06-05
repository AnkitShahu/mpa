from django.shortcuts import render, get_object_or_404, redirect
from myapp.models import Doctor
# Create your views here.


def provider(request):
    Doctors = Doctor.objects.all()
    return render(request, "uindex.html", {"Doctors": Doctors} )

def pdetails(request, slug):
    Doctors = Doctor.objects.all()
    doc = get_object_or_404(Doctors, slug=slug)
    context = {"Doctors": Doctors,
               "doc": doc}
    return render(request, "pdetails.html", context)