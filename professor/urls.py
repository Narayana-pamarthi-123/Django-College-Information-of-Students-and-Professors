from .views import UpdateDetails, firstClassBaseView, Add_Professor, Professor_details, DeleteProfessor
from django.urls import path




urlpatterns = [
    path('addpro/',Add_Professor),
    path('detpro/',Professor_details),
    path('delete/<int:id>',DeleteProfessor),
    path('update/<int:id>',UpdateDetails),
    path('classview/',firstClassBaseView.as_view()),

]