# Are You Alright? Twitter Sentiment Analysis
## Project Description:
------------------------------------
This work focuses on the sentiment analysis of tweets posted by a user on Twitter. We implement Naive Bayes classification model, perceptron and support vector machines to identify the sentiment of each tweet. Based on the sentiment analysis performed on the latest 20 tweets of each individual, we finally detemine if the user feels alright or not. For the detailed report of this project, please refer to the attached [file](report/paper_AI.pdf). 

## To use this software:
------------------------------------
1. Install the libraries in [requirements.txt](requirements.txt) to be able to run the scripts. This can be done by: 
    ```bash
    pip install -r requirements.txt 
    ```  
2. Go to the `src` directory.
3. Run the following command to perform Naive Bayes, dictionary generation and perceptron analyses:

    ```bash
	python3 perceptron.py <input_file(label_list)>  
    python3 main.py <input_file(dataset)> 
    ```  
 
## Feedback, bugs, questions 
-------------------------------
Please reach out to me by email to shahriarhoushmand@gmail.com for any inquiry. Comments and feedbacks are greatly appreciated. 
