from django.shortcuts import render, redirect, get_object_or_404
from .models import Video
from users.models import Account
import difflib

# Create your views here.
# see videos


def account_main(request, id):
    template_name = "videos/account_main_page.html"
    if request.session.get(f'{id}', False):
        if request.method == "POST":

            return redirect(f"/find/{request.POST.get('data')}")

        videos = Video.objects.all()

        return render(request, template_name, {"videos": videos, "account": Account.objects.get(id=id)})

    return redirect("main")


def main(request):

    template_name = "videos/main.html"
    if request.method == "POST":
        return redirect(f"/find/{request.POST.get('data')}")
    videos = Video.objects.all()

    return render(request, template_name, {"videos": videos})


def view(request, id):
    template_name = "videos/view_page.html"
    try:
        video = Video.objects.filter(id=id)[0]

        return render(request, template_name, {"video": video})
    except IndexError:
        return render(request, template_name, {"error": "No such video"})


def account_video(request, id):
    template_name = "videos/account_video_page.html"
    if request.session.get(f'{id}', False):
        videos_of_channel = Video.objects.filter(account=Account.objects.get(id=id))

        return render(request, template_name, {"videos": videos_of_channel, "id": id, "name": Account.objects.get(id=id).username})

    return redirect("login")


def add_video(request, id):
    template_name = "videos/add_video_page.html"
    if request.session.get(f'{id}', False):
        if request.method == "POST":
            account = Account.objects.get(id=id)
            title = request.POST['title']
            cover = request.FILES.get('cover')
            file = request.FILES.get('file')
            if account and title and cover and file:
                video = Video(account=account, title=title, cover=cover, file=file)
                video.save()
                return redirect(f'/account/{id}')

        return render(request, template_name, {"id": id})

    return redirect("login")


def change_video(request, id, video_id):
    template_name = "videos/change_video_page.html"

    if request.session.get(f'{id}', False):
        account = get_object_or_404(Account, id=id)
        video = get_object_or_404(Video, id=video_id, account=account)

        if request.method == "POST":
            title = request.POST.get('title')
            cover = request.FILES.get('cover')
            file = request.FILES.get('file')


            if title:
                video.title = title
            if cover:
                video.cover = cover
            if file:
                video.file = file

            video.save()
            return redirect(f'/account/{id}')

        return render(request, template_name)

    return redirect("login")


def delete_video(request, id, video_id):
    template_name = "videos/delete_video_page.html"
    if request.session.get(f'{id}', False):
        if request.method == "POST":
            video = Video.objects.get(id=video_id)
            video.delete()
            return redirect(f'/account/{id}')

        return render(request, template_name)

    return redirect("login")


def find(request, input_string):
    template_name = "videos/find_page.html"
    videos = []
    for el in Video.objects.all():
        videos.append(el.title)

    closest_match = difflib.get_close_matches(input_string,  videos, n=1)

    if closest_match:
        return render(request, template_name, {"video": Video.objects.get(title=closest_match[0])})

    else:
        return render(request, template_name)


