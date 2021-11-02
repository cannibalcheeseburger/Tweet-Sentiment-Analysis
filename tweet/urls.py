from tweet.views import HomeListView,TweetDetailView
from django.urls import path


urlpatterns = [
    path('',HomeListView.as_view(),name = 'home'),
    path('tweet_detail/<int:pk>',TweetDetailView.as_view(),name = 'tweet_detail'),

]