from django.shortcuts import render
from .models import Shoping
# Create your views here.
def base(request):
    return render(request,'base.html')

def signup(request):
    adminemail="shraddha@gmail.com"
    adminpassword="shraddha"
    email= request.POST.get('email')
    password = request.POST.get('password')
    user=Shoping.objects.filter(email=email)
    if(email==adminemail and password==adminpassword):
        return render(request,'base.html')
    else:
     return render(request,'signup.html')
    
def booking(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        name=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        print(name,email,phone,password,cpassword)
        user = Shoping.objects.filter(email=email)
        if user:
            x = "Email already exist"
            return render(request, 'booking.html', {'msg': x})
        else:
            pass
        if password==cpassword:
            Shoping.objects.create(name=name,email=email,phone=phone,password=password)
            x = "Booking succesfully"
            return render(request,'booking.html',{'msg':x})
        else:
            x = "password and cpassword not match"
            return render(request,'booking.html',{'msg':x,'name':name,'email':email,'phone':phone,})
    else:
        return render(request, 'booking.html')
    

def logout(request):
    return render(request,'signup.html')

def detail(request):
    stu = Shoping.objects.all()
    print(stu)
    return render(request,'detail.html',{'data':stu})

def delete(request,pk):
    data =Shoping.objects.get(id=pk)
    data.delete()
    stu = Shoping.objects.all()
    return render(request, 'detail.html',{'data':stu})

def update(request,pk):
    if request.method=="POST":
         x = Shoping.objects.get(id=pk)
         p = request.POST.get('name')
         q = request.POST.get('email')
         r = request.POST.get('phone')
         s = request.POST.get('password')
         x.name = p
         x.email = q
         x.phone = r
         x.password = s
         x.save()
         stu=Shoping.objects.all()
    x=Shoping.objects.get(id=pk)
    print(x)
    
    return render(request,'update.html',{'data4':x})