from django.urls import path, include
from band import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
	path('', views.all_bands, name='all_bands'),
	path('<int:band_id>/', views.band, name='band'),
	path('api/<int:pk>/', views.BandDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)



'''
url(r'^(?P<band_id>\d+)/$','band.views.band')
path('<int:band_id>/', views.band, name='band')

views.BandDetail.as_view())


'''