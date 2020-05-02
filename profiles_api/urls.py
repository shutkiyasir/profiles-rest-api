from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api.views import HelloAPIView, HelloViewSet, UserProfileViewSet


router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello-viewset')
router.register('profile', UserProfileViewSet)

urlpatterns = [
    path('hello-view/', HelloAPIView.as_view()),
    path('', include(router.urls))
]
