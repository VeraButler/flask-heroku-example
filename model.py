# load the model from disk and return a prediction '1' || '2' || '3'
import pickle


def get_prediction(user_input):
    loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
    return loaded_model.predict([user_input])
