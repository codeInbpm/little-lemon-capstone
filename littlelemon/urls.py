from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restaurant.views import MenuItemViewSet, BookingViewSet
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'api/menu-items', MenuItemViewSet)
router.register(r'api/bookings', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),  # 静态 HTML
    path('api/', include(router.urls)),
    path('api/registration/', include('djoser.urls')),      # 用户注册
    path('api/registration/', include('djoser.urls.token')), # Token 登录
]