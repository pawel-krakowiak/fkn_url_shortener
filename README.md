# SHORT_THIS_F**KING_URL Application
![alt text](https://i.imgur.com/3JuiKk3.png)

## Setup

The first thing to do is to clone the repository:

```sh
$ git https://github.com/pawel-krakowiak/url_shortener.git
$ cd url_shortener
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/app/`.

## Walkthrough

In order to use the application, use the form and shorten your URL. 
If you want to make changes to the domain, change the appropriate values 
in urlgrab/models, and the function accepting the form in grabber_index.html

