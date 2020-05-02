from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api.views import HelloAPIView, HelloViewSet


router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello-viewset')

urlpatterns = [
    path('hello-view/', HelloAPIView.as_view()),
    path('', include(router.urls))
]
