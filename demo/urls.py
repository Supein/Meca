from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mvp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'reserve', views.gameReservation),
    url(r'request', views.gameRequest),
    url(r'currentImage', views.getImage),
    url(r'check', views.checkSolution),
]
