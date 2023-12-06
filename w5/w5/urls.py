"""w5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from w import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.LoginView.as_view()),
    url(r'^register/', views.RegisterView.as_view()),
    url(r'^home/', views.HomeCreatedView.as_view()),
    url(r'^created/', views.CreatedView.as_view()),
    url(r'^exhibit/', views.ExhibitView.as_view()),
    url(r'^site/', views.SiteCreatedView.as_view()),
    url(r'^goods_detail/', views.GoodsDetailCreatedView.as_view()),
    url(r'^search/', views.SearchView.as_view()),
    url(r'^set_password/(?P<username>\w+)/$', views.SetPasswordView.as_view()),
    url(r'^set_avatar/(?P<username>\w+)/$', views.SetAvatarView.as_view()),
    url(r'^backend/(?P<site_name>\w+)/$', views.BackendCreatedView.as_view()),
    url(r'^shop_car/', views.ShopCarView.as_view()),
    url(r'^up_or_down/(?P<pk>\d+)', views.UpOrDownView.as_view()),
    url(r'^comment/', views.CommentView.as_view()),
    url(r'^pay/', views.PayView.as_view()),
    url(r'^cancel/(?P<pk>\d+)', views.CancelView.as_view()),
    url(r'^vip/(?P<username>\w+)/$', views.VipView.as_view()),
    url(r'^add_goods_created/(?P<site_name>\w+)/$', views.AddGoodsCreatedView.as_view()),
    url(r'^add_goods/', views.AddGoodsView.as_view()),
    url(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
]