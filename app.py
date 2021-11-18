from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', bfp=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    weight, chest, abdomen = [x for x in request.form.values()]

    data = []

    weight_lbs = float(weight)*2.20462 
    data.append(float(weight_lbs))
    data.append(float(chest))
    data.append(float(abdomen))
    
    prediction = model.predict([data])
    output = round(prediction[0], 2)

    return render_template('index.html', bfp=output, weight=weight, chest=chest, abdomen=abdomen)


if __name__ == '__main__':
    app.run(debug=True)