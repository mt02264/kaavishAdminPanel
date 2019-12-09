from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from . import views


app_name = "showroom"
urlpatterns = [
	path('login/', views.userLogin, name='login'),
	path('retryLogin/', views.retryLogin, name='retryLogin'),
	path('home/', views.home, name='home'),
	path('logout/', views.userLogout, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

