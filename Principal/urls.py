from django.urls import path, include
from Principal import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import BlogDetail

urlpatterns = [
    path('', login_required(views.index), name='Index'),
    path('aboutme/', login_required(views.aboutme), name='Aboutme'),
    path('accounts/profile/', login_required(views.profile_view), name='Profile'),
    path('createblog/', login_required(views.createblog), name='CreateBlog'),
    path('blogs/', login_required(views.readblog), name='Blogs'),
    path('blogDelete/<blog_author>', views.blogDelete, name='BlogDelete'),
    path('blogUpdate/<blog_author>', views.blogUpdate, name='BlogUpdate'),
    path('blogdetail/<int:pk>/', BlogDetail.as_view(), name='BlogDetail'),
    path('accounts/', include('django.contrib.auth.urls')),


]
