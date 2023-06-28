"""aditivo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#para importar as views dos app
from g_adt import views

urlpatterns = [
    path('admin/', admin.
    site.urls),
    # '' significa que essa sera a pagina inicial, views esta importando do app.nome da função  
    path('', views.home, name='home'),
    # 'nome/' seta o que vem depois da barra do enderenço inicial, para ser buscado , name serve para indentificar a pagina
    path('contato/', views.contato, name='contato')
]
