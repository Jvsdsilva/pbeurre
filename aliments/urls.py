from django.conf.urls import url
from .import views  # import views so we can use them in urls.


urlpatterns = [
    url(r'^$', views.listing),
    url(r'^index', views.index, name="index"),
    url(r'^login/', views.login, name="login"),
    url(r'^results/', views.results, name="results"),
    url(r'^aliment/', views.aliment, name="aliment"),
    url(r'^logout/', views.logout, name="logout"),
    url(r'^mentions/', views.mentions, name="mentions"),
    url(r'^contact/', views.index, name="contact"),
    url(r'^signup/', views.signup, name="signup"),
    url(r'^connected/', views.connected, name="connected"),
    # url(r'^(?P<album_id>[0-9]+)/$', views.detail),
    # url(r'^search/$', views.search),
]
