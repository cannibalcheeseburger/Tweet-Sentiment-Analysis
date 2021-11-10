from django.shortcuts import render,redirect
from .models import tweet
from django.views.generic import ListView,DetailView
from tensorflow.keras.models import load_model
import pickle
from .pred import predict
from .forms import TweetForm

MODEL_PATH ='Dataset/models/'
KERAS_MODEL = MODEL_PATH+"model.h5"
TOKENIZER_MODEL = MODEL_PATH+"tokenizer.pkl"


model = load_model(KERAS_MODEL)
with open(TOKENIZER_MODEL,'rb') as f:
    tokenizer = pickle.load(f)

# Create your views here.

class HomeListView(ListView):
    model = tweet
    template_name = 'home.html'
    context_object_name = 'tweets'
    queryset = tweet.objects.order_by('-date')[:20]

class TweetDetailView(DetailView):
    model = tweet
    template_name = 'tweet_detail.html'
    context_object_name = 'tweet'
    pk = id

def predict_tweet(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TweetForm(request.POST)
        context = {}
        if form.is_valid():
            text = form.cleaned_data['text']
            result = predict(text,model,tokenizer)
            ans = result['score']
            if ans <0.4:
                ans = 0
            elif ans<0.7:
                ans = 2
            else :
                ans = 4
            tweets = {
                'text':text,
                'user':'Anonymous',
                'target': ans,
                'score': result['score']
                }
            context['tweet'] = tweets
            context['form'] = form
        return render(request, 'tweet_detail.html',context)

    form = TweetForm()
    return render(request, 'tweet_form.html',{'form':form})
