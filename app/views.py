from django.shortcuts import render, redirect

from app.models import Person


# Create your views here.

def submit(request, person=None):
    if request.method == 'POST':
        name = request.POST['names']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        weight = request.POST['weight']
        height = request.POST['height']
        gender = request.POST['gender']
        print(name, email, phone, dob,weight,height,gender)
        Person.objects.create(name=name, email=email, phone=phone, dob=dob, weight=weight, height=height, gender=gender)
        count = Person.objects.filter(name=name).count()
        print(f"You have {count} records")
    return redirect('home-page')


def home(request):
    return render(request, 'home.html')


def people(request):
    data = Person.objects.all()
    return render(request,'list.html',{'data':data})


def details(request,id):
    person = Person.objects.get(id=id)
    return render(request,'details.html',{'person':person})


def delete(request,id):
    user = Person.objects.get(id=id)
    user.delete()
    message= f"User {user.name} deleted successfully"
    return redirect('people-page',{'message':message})