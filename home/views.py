from django.shortcuts import render
from django.http import HttpResponse
from home.models import MvMovie
# Create your views here.

def index(request):
	movie_list = MvMovie.objects.all()
	context = {'movie_list':movie_list}
	return render(request, 'templates/movie/index.html',context)
