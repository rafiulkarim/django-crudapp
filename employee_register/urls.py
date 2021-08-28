from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.employee_form, name="employee_form"),
    path('employee-register', views.employee_register, name='process'),
    path('employee-details/<int:id>', views.employee_details, name='details'),
    path('employee-update/<int:id>', views.employee_update, name='update'),
    path('employee-delete/<int:id>', views.employee_delete, name='delete'),
    path('positions', views.position, name='position'),
    path('list/', views.employee_list, name="employee_list"),
]