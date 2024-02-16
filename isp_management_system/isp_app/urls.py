from django.urls import path
from .views import activate_user_view, deactivate_user_view

urlpatterns = [
    path('activate/<str:ip_address>/', activate_user_view, name='activate_user'),
    path('deactivate/<str:ip_address>/', deactivate_user_view, name='deactivate_user'),
]
