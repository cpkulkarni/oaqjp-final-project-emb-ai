''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request 
#from the flask pramework package : TODO
from SentimentAnalysis.sentiment_analysis import emotion_detector 
#function from the package created: TODO

app = Flask("Emotion Detection") 
#Initiate the flask app : TODO

@app.route("/EmotionDetection")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
     # Pass the text to the emotion_detector function and store the response 
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response 
    label = response['label'] 
    score = response['score']

    print(label)
    print(score)

    if label is None:
            return "Invalid input! Try again."
        else:
    # Return a formatted string with the sentiment label and score 
            return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)

# TODO


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')
    #TODO

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000) 
    #TODO
