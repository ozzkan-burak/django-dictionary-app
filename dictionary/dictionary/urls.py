
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from dictionary_app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home)
]
