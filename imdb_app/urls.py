from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from imdb_app import views



urlpatterns = [
	url(r'^$', views.RepoView.as_view(), name="repo_view"),
    url(r'^movies/$', views.movie_list),
    url(r'^movies/(?P<pk>[0-9]+)/$', views.movie_detail),
    url(r'^movies-search/(?P<search_term>[\w\.,_/ \-]+)/$', views.movie_search),
]
urlpatterns = format_suffix_patterns(urlpatterns)
