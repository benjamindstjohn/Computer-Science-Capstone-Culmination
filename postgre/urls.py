from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import users

class loginUser:
 #Metodo de inicio ao sistema de login
   def __init__(self, window, master=None):   
      # Criando o sistema de login
       self.wind = window
       self.wind.title("System F2T")

urlpatterns = [

        #path('', include('main.urls')),
    path('', include('irisApp.urls')),
    path("admin/", admin.site.urls),
  


]
