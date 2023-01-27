from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPanelDashboard.as_view(), name='user_panel_dashboard'),
    path('edit-user', views.EditUserProfilePage.as_view(), name='edit_user_panel'),
    path('change-pass', views.ChangePasswordUser.as_view(), name='change_pass_user')
]
