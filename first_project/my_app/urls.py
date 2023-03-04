from django.urls import path
from my_app.views import Welcome
urlpatterns = [
    path('say/Welcome/',Welcome),
]