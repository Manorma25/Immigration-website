"""
URL configuration for immigration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myapp import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('Login',views.log,name="Login"),
    path('Register',views.reg,name="Register"),
    path('Contactus',views.contact,name="Contact"),
    path('Change_password',views.change,name="change_pw"),
    path('Footer',views.foot),
    path('Forgot',views.forgot),
    path('Help',views.hs,name="help_support"),
    path('',views.index,name="Index"),
    path('Review',views.review,name="review"),
    path('Sidebar',views.side),
    path('Base',views.base),
    path('FAQ',views.faq),
    path('Profile',views.edit,name="editprofile"),
    path('User',views.u_profile,name="myprofile"),
    path('Logout',views.logout,name="logout"),
    path('Detail_Blog/<int:id>',views.detail_blog,name="detailblog"),
    path('Blog',views.blog,name="Blog"),
    path('Visa_detail/<int:id>',views.visa_detail,name="visadetail"),
    path('Visa',views.visa,name="Visa"),
    path('Coaching_details/<int:id>',views.coach_details,name="coachingdetails"),
    path('Coaching',views.coach,name="Coaching"),
    path('Country_details/<str:name>',views.cont_details,name="contdetails"),
    path('Country_details2/<str:name>',views.cont_details2,name="contdetails2"),
    path('Country',views.cont,name="Country"),
    path('News',views.news,name="News"),

    path('Happiness',views.happiness,name="Happiness"),

    path('Happiness1',views.happy1,name="Happiness1"),
    path('Happiness2',views.happy2,name="Happiness2"),
    path('Happiness3',views.happy3,name="Happiness3"),
    path('Happiness4',views.happy4,name="Happiness4"),
    path('Happiness5',views.happy5,name="Happiness5"),
    path('Happiness6',views.happy6,name="Happiness6"),
    path('Happiness7',views.happy7,name="Happiness7"),
    path('Happiness8',views.happy8,name="Happiness8"),
    path('Happiness9',views.happy9,name="Happiness9"),
    path('Happiness10',views.happy10,name="Happiness10"),

    

    path('Human',views.human,name="Human"),

    path('Human1',views.human1,name="Human1"),
    path('Human2',views.human2,name="Human2"),
    path('Human3',views.human3,name="Human3"),
    path('Human4',views.human4,name="Human4"),
    path('Human5',views.human5,name="Human5"),
    path('Human6',views.human6,name="Human6"),
    path('Human7',views.human7,name="Human7"),
    path('Human8',views.human8,name="Human8"),
    path('Human9',views.human9,name="Human9"),
    path('Human10',views.human10,name="Human10"),


    path('Gross',views.gross,name="Gross"),

    path('Gross1',views.gross1,name="Gross1"),
    path('Gross2',views.gross2,name="Gross2"),
    path('Gross3',views.gross3,name="Gross3"),
    path('Gross4',views.gross4,name="Gross4"),
    path('Gross5',views.gross5,name="Gross5"),
    path('Gross6',views.gross6,name="Gross6"),
    path('Gross7',views.gross7,name="Gross7"),
    path('Gross8',views.gross8,name="Gross8"),
    path('Gross9',views.gross9,name="Gross9"),
    path('Gross10',views.gross10,name="Gross10"),

    path('Life',views.life,name="Life"),
   
    path('Life1',views.life1,name="Life1"),
    path('Life2',views.life2,name="Life2"),
    path('Life3',views.life3,name="Life3"),
    path('Life4',views.life4,name="Life4"),
    path('Life5',views.life5,name="Life5"),
    path('Life6',views.life6,name="Life6"),
    path('Life7',views.life7,name="Life7"),
    path('Life8',views.life8,name="Life8"),
    path('Life9',views.life9,name="Life9"),
    path('Life10',views.life10,name="Life10"),

    path('Dashboard',views.dash,name="Dashboard")


    
]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)