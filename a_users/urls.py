from django.urls import path
from .views import profile_view, profile_edit

urlpatterns = [
    path('', profile_view, name='profile'),
    path('edit/', profile_edit, name='profile_edit'),
    path('settings/', profile_edit, name='settings'),  # ✅ เพิ่มบรรทัดนี้
]
