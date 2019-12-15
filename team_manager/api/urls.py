from django.conf.urls import url

from .views import TeamAPIView

urlpatterns = [
    url(r'^$', TeamAPIView.as_view(), name='team-list')
]