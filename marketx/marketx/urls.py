from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('item/', include('item.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('inbox/',include('conversation.urls')),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
