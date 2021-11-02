from tensorflow.keras.models import load_model
import pickle
from pred import predict

MODEL_PATH ='Dataset/models/'
KERAS_MODEL = MODEL_PATH+"model.h5"
TOKENIZER_MODEL = MODEL_PATH+"tokenizer.pkl"


model = load_model(KERAS_MODEL)
with open(TOKENIZER_MODEL,'rb') as f:
    tokenizer = pickle.load(f)

string = input('Enter String: ')
print(predict(string,model,tokenizer))