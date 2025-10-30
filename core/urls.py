
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()

router.register(r'links', views.LinkViewSet, basename='link')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include(router.urls)),
    path('<str:short_code>/', views.short_code_redirect, name='short_code_redirect')
]
