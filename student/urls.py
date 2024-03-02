from .views import UpdateDetails, firstClassBaseView, Add_Student, Student_details, DeleteStudent
from django.urls import path




urlpatterns = [
    path('addFr/',Add_Student),
    path('detFr/',Student_details),
    path('delete/<int:id>',DeleteStudent),
    path('update/<int:id>',UpdateDetails),
    path('classview/',firstClassBaseView.as_view()),

]