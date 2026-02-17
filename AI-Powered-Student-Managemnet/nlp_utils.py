from textblob import TextBlob

#sentiment analysis function
def analyze_sentiment(text:str):
    blob=TextBlob(text) #passed to constructor of the class
    polarity=blob.sentiment.polarity
    
    if polarity>0:
        sentiment="Positive"
    elif polarity<0:
        sentiment="Negative"
    else:
        sentiment="Neutral"
    
    return {
        "polarity":polarity, #float value [-1,1]
        "sentiment": sentiment
    }

#smart seacrh Function (Basic NLP Matching)

def smart_search(students,query:str):
    query=query.lower()
    results=[]
    
    for student in students:
        if(
            query in studentname.lower()
            or query in student.course.lower()
        ):
            results.append(student)
            
    return results