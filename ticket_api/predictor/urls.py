from django.urls import path
from .views import PredictCancellation

urlpatterns = [
    path('predict/', PredictCancellation.as_view(), name='predict')
]
