"""
URL configuration for my_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from blog.views import home_view, about_view, contact_view, post_detail, add_post, edit_post, post_delete
urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='blog-contact'),
    path('about/', about_view, name='blog-about'),
    path('post/<int:post_id>/', post_detail, name='post-detail'),
    path("admin/", admin.site.urls),
    path('post/add', add_post, name='add-post'),
    path('post/<int:post_id>/delete/', post_delete, name='post-delete'),
    path('post/<int:post_id>/edit', edit_post, name='edit-post')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)