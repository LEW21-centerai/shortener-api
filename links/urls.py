from django.urls import path

from . import go, views

urlpatterns = [
    path('go/<slug:shortcut>', go.go),
    path('links/', views.LinkViewSet.as_view({'post': 'create'}))
]
