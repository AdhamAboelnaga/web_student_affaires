from django.urls import path
from .import views
from Home import views as Home
urlpatterns = [
    path('View', views.indexView, name='view'),
    path('Add', views.indexAdd, name='add'),
    path('Search', views.indexSearch, name='search'),
    path('Dept', views.indexDept, name='dept'),
    path('Page1', Home.indexPage1, name='page1'),  # go to login page (page1)
    path('Update', views.indexUpdate, name='update'),



    path('', views.indexStudentAdd, name='studentAdd'),
    path('deleted/<int:id>', views.deleted, name='delete'),
    path('deleteg/<int:id>', views.deleteg, name='delete'),
    path('deletev/<int:id>', views.deletev, name='delete'),


    path('EditStudent/<int:Id>/', views.EditStudent, name='EditStudent'),
    path('updateStudent/<int:Id>/', views.UpdateStudent, name='updateStudent'),
    path('logout', Home.LogoutPage, name='logout'),  # logout



]
