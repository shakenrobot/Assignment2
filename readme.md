## Description

A python movie web application that allows for browsing movies.

## Installation

**Installation via requirements.txt**

```shell
$ cd Assignment2
$ py -3 -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```

## Execution

**Running the application**

From the *CS235FLix* directory, and within the activated virtual environment (see *venv\Scripts\activate* above):

```
python "wsgi.py" (debug=True)

(flask run and python -m flask run (debug=False) aren't working 
working due to ModuleNotFoundError: that I haven't been able to 
find a fix for)

you can still run the project using python "wsgi.py"
```

## Testing

```
python -m pytest
```

http://127.0.0.1:5000

http://127.0.0.1:5000/login

http://127.0.0.1:5000/genres

http://127.0.0.1:5000/genres/<genre>

http://127.0.0.1:5000/actors

http://127.0.0.1:5000/actors/<actor>

http://127.0.0.1:5000/movies

http://127.0.0.1:5000/movies/<movie>

http://127.0.0.1:5000/directors

http://127.0.0.1:5000/directors/<director>
