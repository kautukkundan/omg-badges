# OMG Badges 🎉

<img width="1440" alt="Screenshot 2020-07-04 at 8 38 03 PM" src="https://user-images.githubusercontent.com/23727056/86515413-544c0100-be36-11ea-80bb-f836584da32a.png">

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
    - [Setting up the app](#setting-up-the-app)
      - [Setting up Oauth2 for Google Sign-in](#setting-up-oauth2-for-google-sign-in)
      - [Adding badges](#adding-badges)
      - [Adding sessions](#adding-sessions)
      - [Adding Count Special Badges](#adding-count-special-badges)
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
4. At the root of your project directory <br>
```bash 
pip install -r requirements.txt
```

5. create a file ```.env``` and copy contents of ```.env_dummy``` to ```.env``` in the same directory
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
6. You can use [https://djecrety.ir/] to generate your secret key
7. Set ```PRODUCTION=False``` during development in ```.env``` file otherwise enter the db details.
8. Get Google Oauth2 client key and Secret key and enter it here. Follow this for the same https://developers.google.com/identity/protocols/oauth2
9. **Make sure to not have give spaces between KEY=VALUE**

10. After the above setup, run <br>
```
python manage.py makemigrations
python manage.py migrate
```

11. Create superuser <br>
```
python manage.py createsuperuser
```
make sure to enter all the details including email

12. Start the backend server (testing server)
```
python manage.py runserver
```
Runs the backend server at default port ```8000```.<br />
Open [http://localhost:8000](http://localhost:8000) to view it in the browser.

### Setting up the app

#### Setting up Oauth2 for Google Sign-in
1. log into [http://localhost:8000/admin](http://localhost:8000/admin)
2. Go to **DJANGO OAUTH TOOLKIT > Applications**
3. click **Add Application**
4. Copy **Client ID** for later use
5. Click search icon next to user and select your superuser
6. leave **redirect URIs** > blank
7. select **Client Type** > public
8. select **Authorization grant type** > Resource owner password-based
9. Give whatever name to the application (maybe "Gauth")
10. It should look something like this after setup.
    
<img width="1192" alt="Screenshot 2020-07-04 at 8 51 00 PM" src="https://user-images.githubusercontent.com/23727056/86515649-1cde5400-be38-11ea-9a0f-2a4c05c72227.png">

#### Adding badges
1. log into [http://localhost:8000/admin](http://localhost:8000/admin)
2. Go to **BADGES > Badges**
3. click **Add Badge**
4. **BadgeId** - give any id to the badge, a short one word description recommended
5. **Name** - give full name of the badge, It'll be displayed on the app
6. Select any image for the badge. Recommended square and small size ~70kb

#### Adding sessions
1. log into [http://localhost:8000/admin](http://localhost:8000/admin)
2. Go to **EVENTS > Sessions**
3. click **Add Sessions**
4. **SessionId** - give any id to the session, a short one word description recommended
5. **Name** - give full name of the session
6. **Badge** - associate badge to this session
7. **Track** - default 1, change this number for multiple parallel tracks.
8. **start**, **end** - Set start time and end time for the session. **Please be careful while adding these details as badges depends on this**

#### Adding Count Special Badges
This is used to provide badges when a user attends a set number of sessions. 
eg- Attended 5 sessions, Attended 20 sessions. 

1. log into [http://localhost:8000/admin](http://localhost:8000/admin)
2. Go to **EVENTS > Session count specials**
3. click **Add Session count specials** 
4. select **count**
5. select associated badge

### API Reference