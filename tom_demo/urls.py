from django.urls import path

from tom_demo.views import CustomObservationCreateView

app_name = 'tom_demo'

urlpatterns = [
    path('<str:facility>/create/', CustomObservationCreateView.as_view(), name='create'),
]
