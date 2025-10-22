"""
URL configuration for chaiheadq project.
"""
import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from tweet import views
from tweet.views import TweetListView

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Tweet app URLs
    path('tweet/', include('tweet.urls')),

    # User registration
    path('register/', views.register, name='register'),

    # User login
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # Authentication URLs (logout, password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),

    # Homepage (tweet list)
    path('', TweetListView.as_view(), name='tweet_list'),
]

# Serve media files during development and on Render
if settings.DEBUG or os.environ.get("RENDER"):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
