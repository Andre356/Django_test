from django.urls import path
from . import views

from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'groupsset', views.MyGroupsViewSet)
router.register(r'usersset', views.MyUsersViewSet)


urlpatterns = [
    path('home', views.home, name='home'),

    path('new_user', views.new_user, name='new_user'),
    path('edit_user/<int:id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),

    path('new_group', views.new_group, name='new_group'),
    path('edit_group/<int:id>/', views.edit_group, name='edit_group'),
    path('delete_group/<int:id>/', views.delete_group, name='delete_group'),

    url(r'^', include(router.urls)),
]
