from django.conf.urls import url
from .views import HomeView, BoardView, SocietyView, SenateView, ContactListView, ContactView, OfficeView

app_name = 'main'

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^office-bearers/$', OfficeView.as_view(), name='office-bearers'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^contact_list/$', ContactListView.as_view(), name='contact_list'),
    url(r'^board/(?P<slug>[\w-]+)/$', BoardView.as_view(), name='board-detail'),
    url(r'^senate/(?P<slug>[\w-]+)/$', SenateView.as_view(), name='senate-detail'),
    url(r'^society/(?P<slug>[\w-]+)/$', SocietyView.as_view(), name='society-detail'),
]
