
from django.contrib import admin
from django.urls import path

from women.views import *
from django.urls import path, include
# from women.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('women/', include('women.urls')),


    # path('', index),
    # path('cats/', categories),
]

handler404 = pageNotFound
handler403 = permission_denied
handler400 = bad_request
handler500 = server_error

