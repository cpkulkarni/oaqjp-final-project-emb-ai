''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request 
#from the flask pramework package : TODO
from EmotionDetection.emotion_detection import emotion_detector 
#function from the package created: TODO


app = Flask("Emotion Detection") 
#Initiate the flask app : TODO

@app.route("/emotionDetector")
def emotion_detector_fn():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
     # Pass the text to the emotion_detector function and store the response 
    response = emotion_detector(text_to_analyze)

    # Extract the details from the response 
    response_1 = response.copy()
    response_1.pop("dominant_emotion", None)
    output_text = "For the given statement, the system response is "

    *rest, (last_key, last_value) = response_1.items()
    joined_rest = ", ".join(f"'{k}': {v}" for k, v in rest)
    output_text = output_text + joined_rest + " and '" + str(last_key) + "': " + str(response.get(last_key))

    output_text = output_text + ".\n The dominant emotion is " + str(response.get('dominant_emotion')) + "."
    

    if output_text is None:
        return "Invalid input! Try again."
    else:
    # Return a formatted string with the sentiment label and score 
        return output_text




@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000) 

