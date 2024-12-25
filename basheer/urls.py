from django.contrib import admin
from django.urls import path
from crudoperationsapp.views import *
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index),
    path('', receipes, name='receipes'),
    path('delete_receipe/<id>/', delete_receipe, name='delete_receipes'),
    path('update_receipe/<id>/', update_receipe, name='update_receipes'),
    path('login/', login_page, name="login_page"),
    path('logout/', logout_page, name="logout_page"),
    path('register/',register_page, name="register"),
]
if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)