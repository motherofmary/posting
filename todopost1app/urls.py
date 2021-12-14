
from django.urls import path
from . import views
urlpatterns = [
    path('reg',views.reg,name="reg"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('', views.fun, name='fun'),
    path('task_view', views.task_view, name='task_view'),

    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),

]