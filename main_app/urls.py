from django.urls import path
from main_app.views import (
    email,
    about_list,
    shop_list,
    shop_detail,
    service_list,
    blog_list,
    blog_detail,

    ContactView,
    CreateViewShop,
    ShopDeleteView,
    ShopUpdateView,
    BlogCreateView,
    BlogDeleteView,
    BlogUpdateView
)

urlpatterns = [
    path('about/', about_list, name='about'),
    path('email/', email, name='email'),
    path('shop/', shop_list, name='shop'),
    path('shop/<slug:slug>/', shop_detail, name='shop_detail'),
    path('services/', service_list, name='service'),
    path('contact/', ContactView.as_view(), name='contact'),


    path('blogs/', blog_list, name='blog'),
    path('blog-create/', BlogCreateView.as_view(), name='blog-create'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blogs/<int:pk>/', blog_detail, name='blog_detail'),


    path('create/', CreateViewShop.as_view(), name='create'),
    path('<slug:slug>/delete/', ShopDeleteView.as_view(), name='project_delete'),
    path('project-edit/<slug:slug>/', ShopUpdateView.as_view(), name='projects-edit'),
]
