from django.shortcuts import render, redirect
from .models import make_password, Account
# Create your views here.
# create account
# log in account
# delete account


def create(request):
    template_name = "users/create_page.html"
    if request.method == "POST":
        username = request.POST['username']
        if Account.objects.filter(username=username).exists():
            return render(request, template_name, {"error": "Username is already taken"})
        password = make_password(request.POST['password'])
        account = Account(username=username, password=password)
        account.save()
        user = Account.objects.filter(username=username)
        request.session[f"{account.id}"] = 'True'
        return redirect(f"/account_main/{user[0].id}")

    return render(request, template_name)


def login(request):
    template_name = "users/login_page.html"

    if request.method == "POST":
        username = request.POST['username']
        password = make_password(request.POST['password'])

        if Account.objects.filter(username=username).exists():
            user = Account.objects.filter(username=username)

            if user[0].password == password:
                request.session[f"{user[0].id}"] = 'True'

                return redirect(f"/account_main/{user[0].id}")
            return render(request, template_name, {"error": "Password is not valid"})
        return render(request, template_name, {"error": "Username is not valid"})
    return render(request, template_name)


def delete(request):
    template_name = "users/delete_page.html"

    if request.method == "POST":
        username = request.POST['username']
        password = make_password(request.POST['password'])

        if Account.objects.filter(username=username).exists():
            user = Account.objects.filter(username=username)

            if user[0].password == password:
                del request.session[f"{user[0].id}"]
                user.delete()
                return redirect("main")
            return render(request, template_name, {"error": "Password is not valid"})
        return render(request, template_name, {"error": "Username is not valid"})
    return render(request, template_name)