from django.shortcuts import render
from band.models import Band
from rest_framework import generics
from band.serializers import BandSerializer

def all_bands(request):
	return render(request, 'band/all_bands.html')
	
class BandDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Band.objects.all()
	serializer_class = BandSerializer


# Create your views here.
def band(request, band_id):
	band = Band.objects.get(pk=band_id)
	return render(request, 'band/band.html',{'band':band})
