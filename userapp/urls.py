from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from userapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('about_us/', views.about_us, name='about_us')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)