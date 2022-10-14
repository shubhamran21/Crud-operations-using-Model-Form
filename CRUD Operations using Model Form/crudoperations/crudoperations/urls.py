from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.addandshow, name="addandshow"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('update/<int:id>/', views.update, name="update"),
    
]
 