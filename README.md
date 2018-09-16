# Topic classification for Twitter Data

<!--Hypothesis:-->
<!--Is it viable to build a recommendation hashtag system with machine learning algorithms-->

Explore the performance of a hashtag recommendaton system with machine learning algorithms (specifically Naive Bayes, Decision Trees and Random forests).
Then deploying the best performing algorithm onto a web app, where the web app will allow the user to make twitter user timeline requests and perform a classification on the messages retrieved.

## Getting Started
Download repository:
```
git clone git@github.com:kankyu/topic_classification_for_twitter_data.git
```

python version:
```
python -v # 2.7.12
```

Install Dependencies:
```
pip -r install requirements.txt
```

Collect hashtags for specfic tweets:
```
cd app/Modules/
python collect_data.py
```

In app/Modules/ create `data` folder and move the collected tweets into it:
```
mkdir data/
mv #*.txt data/
```


<!--Improvements that can be made-->
<!--Data engineering-->

