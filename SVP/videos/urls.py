from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("main", views.main, name="main"),
    path("account_main/<id>", views.account_main, name="account_main"),
    path("view/<id>", views.view),
    path("account/<id>", views.account_video),
    path("account/add/<id>", views.add_video),
    path("account/change/<id>/<video_id>", views.change_video),
    path("account/delete/<id>/<video_id>", views.delete_video),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
