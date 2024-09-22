from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainapp/', include('main_app.urls')),
    path('cart/', include('cart.urls')),
    path('total/', include('total.urls')),
    path('users/', include('users.urls')),
    path('', include('homepage.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
