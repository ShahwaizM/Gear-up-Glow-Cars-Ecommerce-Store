from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from . import settings
from django.contrib.auth.models import  Group
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('store.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = "Gear Up & Glow Admin"
admin.site.site_title = "Gear Up & Glow Admin Portal"
admin.site.index_title = "Welcome to Gear Up & Glow Admin Portal"
admin.site.unregister(Group)