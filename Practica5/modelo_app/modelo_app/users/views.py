import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import User


def index(request):
    return render(request, 'base/index.html')

def indexUsers(request):
    users = User.objects.all()
    return render(request, 'users/index.html', {'users': users})

def createUserView(request):
    return render(request,"users/create.html")

def createUser(request):
    data = {}
    try: 
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            age = request.POST.get("age")
            rfc = request.POST.get("rfc")
            photo = request.POST.get("photo")

            user = User(name=name, email=email, age=age, rfc=rfc, photo=photo)
            user.save()
            data["user"]=user
            data["message"] = "User created"
            data["status"] = "success"
    except Exception as e:
        data["message"]= str(e)
        data["status"]= "error"


        return render(request, "users/create.html", data)

def userDetail(request, id):
    user = get_object_or_404(User, id=id)
    #user = User.objects.get(id=id)
    data = {
        "user": user
    }
    return render(request, "users/detail.html",data)

def createUserByFetch(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    return JsonResponse(
        {
            "NOMBRE RECIBIDO": body.get("name")
        }
    )

def edit_user(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'users/edit.html', {'user': user})

def update_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.age = request.POST['age']
        user.rfc = request.POST['rfc']
        user.photo = request.POST['photo']
        user.save()
        return redirect('index')
    return render(request, 'users/edit.html', {'user': user})

def orders(request):
    return render(request, 'orders/index.html')