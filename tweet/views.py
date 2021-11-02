from django.shortcuts import render
from .models import tweet
from django.views.generic import ListView,DetailView

# Create your views here.

class HomeListView(ListView):
    model = tweet
    template_name = 'home.html'
    context_object_name = 'tweets'
    queryset = tweet.objects.order_by('-date')[:15]

class TweetDetailView(DetailView):
    model = tweet
    template_name = 'tweet_detail.html'
    context_object_name = 'tweet'
    pk = id
