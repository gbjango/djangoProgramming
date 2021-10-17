"""djangostagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from dsuser.views import RegisterView, index, LoginView, logout
from post.views import PostDetail, PostList, PostCreate

# 이미지를 업로드하자
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/register/',RegisterView.as_view(), name='register'),
    path('user/login/', LoginView.as_view(), name='login'),
    path('', PostList.as_view()),
    path('post/<int:pk>', PostDetail.as_view(), name='post'),
    path('upload/', PostCreate.as_view(), name='upload'),
    path('logout/', logout, name='logout'),
]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)