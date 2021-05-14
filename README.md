# Fake-News-Detection
This is a project which can detect all types of fake news including ClickBait.

![Python](https://img.shields.io/badge/python%20-%23323330.svg?&style=for-the-badge&logo=python&logoColor=%23F7DF1E) ![Django](https://img.shields.io/badge/flask%20-%23092E20.svg?&style=for-the-badge&logo=flask&logoColor=white) ![HTML5](https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white") 


### Problem Statement
Fake news is fake or misleading information presented as news or say Fake News may be a spread of disinformation and hoaxes through any news platform.The approaching threat of such widespread misinformation is clear.
The two types can be classified as follows:

- Fake-News: are those news stories/articles that are false: the story/article itself is fabricated, with no verifiable facts, sources or quotes.

- Clickbait News: is defined as content whose main purpose is to draw attention and encourage visitors to click on a link to a specific website. 

# Models


## Dataset:
- The clickbait dataset contains, only two attributes: 
> Tagline: The main heading of the content

  ClickBait: (0 or 1) weather the given news in clickbaited or not.


- The Fake news articles contains 6 attributes, the main attributes are:
> Title: Title of the article.

  Text: Content of the news article

  Label: Indicates news article is fake or not


# Accuracy

# How to Run?

Just run the following commands:
```
$ pip install -r requirements.txt
$ python app.py
```
Just this and you are good to go

# Website

We also made a GUI in the form of the website for the detector. The Backend is made using Flask, whereas the frontend is normal HTML and CSS.

### Fake News Detector
![Fake-News-Detector](./demo_assets/fakenews.JPG)

### Clickbait Detector
![Clickbait-Detector](./demo_assets/clickbait.JPG)

### Short Demo (Please Give it sometime to Load 😃)
![Demo_Video](./demo_assets/demo.gif)


## Refrences
> Dataset and Features: 

- https://www.kaggle.com/c/fake-news/data?select=train.csv (Fake-News-Dataset)
- https://www.kaggle.com/amananandrai/clickbait-dataset (Clickbait Dataset)

> Research Papers:

- For FakeNews:
    - https://www.ijitee.org/wp-content/uploads/papers/v8i11/K18290981119.pdf
    - https://link.springer.com/chapter/10.1007%2F978-981-15-8354-4_26
- For Clickbait:
    - https://link.springer.com/chapter/10.1007/978-3-319-30671-1_72
    - https://cutt.ly/2bdhA9p



# Future Scope
- Integration of this service in a form of plugin in social media website/apps to prevent spreading of misinformation and changing people views during election.
- Implementing this with Fake Indian Political News so that there is less misinformation.

