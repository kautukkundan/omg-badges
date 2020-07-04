# OMG Badges 🎉

OMG badges is an open-source app for distributing badges to attendees while watching your event's live stream. This app was built for https://dscomg.com and now is open to all communities to utilise in their own meetup/event/etc.

What does OMG badges do?
* Gamification for attendees. It engages attendees as they have more to do than just attending the sessions.
* Give session badges or standalone badges.
* Auto Badges on attending a set number of sessions (5 sessions, 20 sessions)
* Hide easter eggs on your website and provide badges on finding them.
* Be creative and Have fun! 

## Documentation 📄
Documentation is hard. I have tried my best to list everything in detail but please feel free to ask any questions in the issues.

- [OMG Badges 🎉](#omg-badges-)
  - [Documentation 📄](#documentation-)
    - [Getting Started](#getting-started)
    - [API Reference](#api-reference)


### Getting Started

1. clone the repo
2. Go in the repo and setup virtual environment using <br>
```python -m venv env``` 
3. Then activate the environment using <br>
    - On Windows
```source env\Scripts\activate```
    - On MacOS/Linux
```source env/bin/activate```
- At the root of your project directory <br>
```bash 
pip install -r requirements.txt
```

4. create a file ```.env``` and copy contents of ```.env_dummy``` to ```.env``` in the same directory
```
SECRET_KEY=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
GOOGLE_OAUTH2_KEY=
GOOGLE_OAUTH2_SECRET=
PRODUCTION=
```
5. You can use [https://djecrety.ir/] to generate your secret key
6. Set ```PRODUCTION=False``` during development in ```.env``` file otherwise enter the db details.
7. Get Google Oauth2 client key and Secret key and enter it here. Follow this for the same https://developers.google.com/identity/protocols/oauth2
8. **Make sure to not have give spaces between KEY=VALUE**

9. After the above setup, run <br>
```
python manage.py makemigrations
python manage.py migrate
```

10. Create superuser <br>
```
python manage.py createsuperuser
```
make sure to enter all the details including email

11. Start the backend server (testing server)
```
python manage.py runserver
```
Runs the backend server at default port ```8000```.<br />
Open [http://localhost:8000](http://localhost:8000) to view it in the browser.


### API Reference