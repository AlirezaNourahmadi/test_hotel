from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list_view, name='room_list'),  # 📄 لیست همه اتاق‌ها
    path('<int:pk>/', views.room_detail_view,name='room_detail'),  # 🔍 جزییات یک اتاق

    # 👇 فقط مدیر می‌تونه اینا رو ببینه
    path('create/', views.room_create_view,name='room_create'),  # ➕ ایجاد اتاق
    path('<int:pk>/edit/', views.room_update_view,name='room_update'),  # ✏️ ویرایش اتاق
    path('<int:pk>/delete/', views.room_delete_view,name='room_delete'),  # 🗑️ حذف اتاق
]
