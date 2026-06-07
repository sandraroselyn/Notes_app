
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('notes_list/',views.notes_list,name='notes_list'),
    path('update/<int:id>/',views.update_notes,name='update_notes'),
    path('delete/<int:id>/',views.delete_notes,name='delete_notes'),
    path('',views.login_page,name='login_page'),
    path('register/',views.register_page,name='register_page'),

]