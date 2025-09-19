"""
URL configuration for gShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .forms import LoginForm
from django.conf.urls.i18n import i18n_patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('blog_detal/', views.blog_detail, name="blog_detail"),
    path('blog/', views.blog, name="blog"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('contact/', views.contact, name="contact"),
    path('detail/', views.detail, name="detail"),
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html", authentication_form=LoginForm), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('product/', views.product, name="product"),
    path('about/', views.about, name="about"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('wishlist/add/<int:pk>', views.add_to_wishlist, name="add_to_wishlist"),
    path('wishlist/remove/<int:pk>', views.remove_from_wishlist, name="remove_from_wishlist"),
    path('accounts/profile/', views.profile, name="profile"),
    path('i18n/', include('django.conf.urls.i18n')),
    path('price-api/<str:asset_key>/', views.price_api, name='price_api'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
