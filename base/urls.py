from django.urls import path
from . import views
urlpatterns = [
    
    path('home',views.home,name='home'),
    path('login_page',views.login_page,name='login_page'),
    path('notes',views.notes,name='notes'),
    path('list_create',views.list_create,name='list_create'),
    path('register_page',views.register_page,name='register_page'),
    path('logout1',views.logout1,name='logout1'),
    path('delete/<int:pk>',views.note_delete,name='delete'),
]

