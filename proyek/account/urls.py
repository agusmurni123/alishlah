from django.urls import path
from . import views


app_name = 'artikel'

urlpatterns=[
    path('user/',views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('register', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('staff/', views.staff, name='staff'),
    path('', views.IndexBlog.as_view(),name='konten'),
    path('tambah/',views.TambahBlog.as_view(),name='tambah'),
    path('detail/<pk>',views.DetailBlog.as_view(),name='detail'),
    path('delete/<pk>/',views.HapusBlog.as_view(),name='hapus'),
    path('edit/<pk>/',views.UbahBlog.as_view(),name='ubah'),
]
