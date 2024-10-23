from django.urls import path
from . import views

urlpatterns=[
      path('dashboard/',views.index,name='dashboard-index'),
      path('staff/',views.staff,name='dashboard-staff'),
      path('order/',views.order,name='dashboard-order'),
      path('product/',views.products,name='dashboard-product'),
      path('product/delete/<int:pk>',views.product_delete,name='dashboard-product_delete'),
      path('product/update/<int:pk>',views.product_update,name='dashboard-product_update'),
       path('staff/detail/<int:pk>',views.staff_detail,name='dashboard-staff_detail'),









] 