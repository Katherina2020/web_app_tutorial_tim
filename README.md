# web_app_tutorial_tim
I failed to add the directorys correctly. I don't know how to fix this at this moment.
The structure should be like this:
Directory with any name that you want (I use FLASK_WEB_APP_TUTORIAL_TIM).
Inside this directory is main.py and directory website.
And inside website directory are:
templates
__init__.py
auth.py
views.py
I run main.py without arguments.
I start the server and go to sign up page, fill out input forms and press submit. And become RuntimeError
RuntimeError: The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.
(I try to print out flash message).
If i change in auth.html str 31 to 30(print instead flash) programm works correctly.
127.0.0.1 - - [09/May/2021 16:06:57] "POST /sign-up HTTP/1.1" 200 -
ImmutableMultiDict([('email', ''), ('firstName', ''), ('password1', ''), ('password2', '')])
email 
first name 
password1 
password2 
Email must be greater that 3 characters

I don't understand why my flash message doesn't work. The secret key is unique and is given in __init__.py
