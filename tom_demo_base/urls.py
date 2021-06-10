"""django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('alerts/', include('tom_alerts_dash.urls', namespace='tom_alerts_dash')),
    path('superevents/', include('tom_superevents.urls')),
    path('observations/', include('tom_demo.urls')),
    path('', include('tom_common.urls')),

    # Vue health check urls
    path('vue_health_check/', TemplateView.as_view(template_name="vue_health_check.html"), name="vue_health_check"),

    path("vue_app_01/", TemplateView.as_view(template_name="vue_app_01.html"), name="vue_app_01"),
    path("vue_app_02/", TemplateView.as_view(template_name="vue_app_02.html"), name="vue_app_02"),

    # TODO: should probably be removed
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
]

# this is to serve static file from a debug Dockerfile environment (with collectstatic)
# (i.e. without this a local Dockerfile-deployed instance won't find the staticfiles from
# the other INSTALLED_APPS)
urlpatterns += staticfiles_urlpatterns()
