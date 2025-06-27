"""
URL patterns for the listing app

THis file will contain the URL patterns related to the travel app
More API endpoints will be added during development
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

url_patterns = [
    path('', include(router.urls)),
]

app_name = "listings"
