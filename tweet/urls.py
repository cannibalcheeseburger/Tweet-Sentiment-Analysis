from tweet.views import HomeListView,TweetDetailView,predict_tweet
from django.urls import path


urlpatterns = [
    path('',HomeListView.as_view(),name = 'home'),
    path('tweet_detail/<int:pk>',TweetDetailView.as_view(),name = 'tweet_detail'),
    path('predict/',predict_tweet,name = 'predict_tweet'),

]