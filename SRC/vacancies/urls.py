from django.urls import path
from .import views

urlpatterns = [
    path('cvacancy/',views.cvacancy, name= "createvacancy"),
    path('jrecruiting/',views.jrecuriting, name= "jrecruiting"),
    path('uvacancy/',views.uvacancy, name="update vacancy"),
    path('deletecon/',views.deletecon, name="delete confirmation"),

    path('updatecom/<str:pk>/',views.updateComVa, name="updatecom"),
    path('deletecom/<str:pk>/',views.deleteComVa, name="deletecom"),

    #path('createvacancy/',views.createvacancy, name="createvacancy"),


    # diliya

    path('button/', views.readcvbtn, name="button"),
    path('ogcreatehtml/', views.ogcreatehtml, name="ogcreatehtml"),
    path('updatecv/<str:pk>/', views.updatecv, name="updatecv"),
    path('deletecv/<str:pk>/', views.deleteCv, name="deletecv"),

]