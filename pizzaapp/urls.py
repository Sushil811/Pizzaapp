from django.contrib import admin
from django.urls import path
from .views import userorders, acceptorders, declineorders, adminorders,placeorder, userlogout, userauthenticate, customerwelcomeview, adminloginview, userloginview, signupuser, adminhomepageview, authenticateadmin, logoutadmin, addpizza, deletepizza, homepageview


urlpatterns = [
    path('admin/', adminloginview, name='adminloginpage'),
    path('adminauthenticate/', authenticateadmin),
    path('admin/homepage/', adminhomepageview, name='adminhomepage'),
    path('adminlogout/', logoutadmin),
    path('addpizza/',addpizza),
    path('deletepizza/<int:pizzapk>/',deletepizza),

    path('',homepageview, name='homepage'),
    path('signupuser/', signupuser),

    path('loginuser/', userloginview, name='userloginpage'),
    path('customer/welcome/', customerwelcomeview, name='customerpage'),
    path('customer/authenticate/', userauthenticate),
    path('userlogout/', userlogout),
    path('placeorder/', placeorder),
    path('userorders/', userorders),
    path('adminorders/', adminorders),
    path('acceptorders/<int:orderpk>/', acceptorders),
    path('declineorders/<int:orderpk>/', declineorders)
]
