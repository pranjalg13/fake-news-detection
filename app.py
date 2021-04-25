from flask import Flask
import tensorflow as tf
from flask import Flask, render_template, request, redirect
from wtforms import Form, TextField, validators, SubmitField, DecimalField, IntegerField
from utils import get_encoded_text
from keras.models import load_model
import pickle
import gzip

app = Flask(__name__)

class ReusableForm(Form):
    """User entry form for entering specifics for generation"""
    # Starting seed
    # seed = TextField("Enter a seed string or 'random':", validators=[
    #                  validators.InputRequired()])
    title = TextField("Enter the Article title", validators=[
        validators.InputRequired(), validators.Length(min=10,max=50)
    ])
    articletext = TextField("Enter the text of Article", validators=[
        validators.InputRequired(), validators.Length(min=20,max=5000)
    ])
    # # Diversity of predictions
    # diversity = DecimalField('Enter diversity:', default=0.8,
    #                          validators=[validators.InputRequired(),
    #                                      validators.NumberRange(min=0.5, max=5.0,
    #                                                             message='Diversity must be between 0.5 and 5.')])
    # # Number of words
    # words = IntegerField('Enter number of words to generate:',
    #                      default=50, validators=[validators.InputRequired(),
    #                                              validators.NumberRange(min=10, max=100, message='Number of words must be between 10 and 100')])
    # Submit button
    submit = SubmitField("Submit")

# def load_keras_model():
#     """Load in the pre-trained model"""
#     global model
#     model = load_model('../trained_models/final_h5_model.h5')
#     # Required for model to work
#     global graph
#     graph = tf.get_default_graph()

# global graph
global model
model = load_model('./trained_models/final_h5_model.h5')
# Required for model to work
global loaded_model
loaded_model = pickle.load(open('./trained_models/clickbait_model.pkl','rb'))


@app.route("/result",methods=['POST'])
def getresult():
    form = ReusableForm(request.form)

@app.route("/",methods=['GET', 'POST'])
def indexpage():
    fakestring = ""
    form = ReusableForm(request.form)
    if request.method == "POST" and form.validate():
        rtitle = request.form['title']
        rarticletext = request.form['articletext']
        encoded_value = get_encoded_text(rarticletext)
        print(encoded_value)
        prediction = model.predict_classes(encoded_value)
        isfake = prediction[0][0]
        if(isfake==0):
            fakestring = "You Are Reading a Fake News, Check you sources man."
        else:
            fakestring = "Nice, Your Sources of News are correct"
        print(prediction[0][0])        
        return render_template("result.html",predict = fakestring)
        # return render_template('index.html',form = form, predict = fakestring)
        # print(request.form['title'])
    else:
        return render_template('index.html',form = form)

@app.route('/clickbait-home')
def homepage():
    return render_template('clickbait-index.html')

@app.route('/clickbait-check',methods=['POST'])
def checkClickbait():
    title=request.form['title']
    if not title:
        pass
    
if __name__ =='__main__':
    app.run(debug=True)