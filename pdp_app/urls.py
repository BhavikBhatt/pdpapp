from django.conf.urls import url, include
from pdp_app import views

app_name = 'pdp_app'

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^qa/$', views.PostListView.as_view(), name='posts'),
    url(r'^qa/(?P<pk>\d+)', views.PostDetailView.as_view(), name='post-detail'),
    url(r'^add_post/', views.add_post, name='addpost'),
    url(r'^add_comment/(?P<pk>\d+)$', views.add_comment, name='addcomment'),
    url(r'^remove_post/(?P<pk>\d+)/$', views.PostDelete.as_view(), name='removepost'),
    url(r'^state/(?:(?P<state_name>.+)/)?$', views.state, name='state-detail'),
]