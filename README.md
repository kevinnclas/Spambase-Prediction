# Implementation of a Machine Learning model detecting spam mails

For this project, the main task was to create a Machine Learning model able to diffrenciate a spam from a real mail and implement it into an API.

## Machine Learning model
<br/>

Here is the common process when applying machine learning to real-world data as defined by Yufeng Guo [here](https://towardsdatascience.com/the-7-steps-of-machine-learning-2877d7e5548e).

<br>

![Process](https://i.imgur.com/mqTCqBR.png)

<br>

The first step of this project was to collect the data and prepare it. As this kind of problem already has been solved in the past, it was easy to find a good and cleaned dataset. We use the [Spambase](https://archive.ics.uci.edu/ml/datasets/Spambase) dataset accesible on the [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php).

The next steps of the process are done on a Jupyter notebook that you can see inside this repository. On this Jupyter notebook you will find the following steps:
* The analysis of the data
* A first evaluation of several models
* The tuning of chosen models.
* The selection of the final model and its predictions


## API Implementation
<br/>
After the creation and selection of our final model, we decide to implement it into an API. How it works? You just have to write or paste a mail in the dedicated field, and then the API shows you the given prediction made by our model.


## Launch the Flask Application with Docker
<br/>
If you have installed Docker on your machine you can launch the flask application with those command in powershell or cmd.
<br>
```
> docker pull ikhlo/spam
> docker run -p 5000:5000 ikhlo/spam
```














