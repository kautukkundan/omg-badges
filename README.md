# OMG Badges 🎉

<img width="1440" alt="Screenshot 2020-07-04 at 8 38 03 PM" src="https://user-images.githubusercontent.com/23727056/86515413-544c0100-be36-11ea-80bb-f836584da32a.png">

OMG badges is an open-source gamification framework for distributing badges to attendees while watching your event's live stream. This app was built for https://dscomg.com and now is open to all communities to utilise in their own meetup/event/etc.

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
    - [Getting Started 🏃‍♀️🏃‍♂️](#getting-started-️️)
    - [Setting up the app 👩‍💻👨‍💻](#setting-up-the-app-)
      - [Setting up Oauth2 for Google Sign-in](#setting-up-oauth2-for-google-sign-in)
      - [Adding badges](#adding-badges)
      - [Adding sessions](#adding-sessions)
      - [Adding Count Special Badges](#adding-count-special-badges)
    - [API Reference 🌐](#api-reference-)
      - [Exchanging Access Token](#exchanging-access-token)
      - [Marking Attendance in a session](#marking-attendance-in-a-session)
      - [Fetching Sessions of a user](#fetching-sessions-of-a-user)
      - [Granting Individual Badges](#granting-individual-badges)
      - [Fetching Badges of a user](#fetching-badges-of-a-user)
      - [Fetching Badges/Session using Public profile](#fetching-badgessession-using-public-profile)
    - [Deployement 📦](#deployement-)
    - [Known Issues and Notes 🐞](#known-issues-and-notes-)


### Getting Started 🏃‍♀️🏃‍♂️

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
7. Set ```PRODUCTION=False``` during development in ```.env``` file otherwise enter the db details. If you wish to use SQLite3 for production db, in that case also leave ```PRODUCTION=False``` and ignore any other DB_* fields. Keep in mind that the app will run in debug mode if ```PRODUCTION=False```. 
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

### Setting up the app 👩‍💻👨‍💻

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

You can use the badges in 2 ways 
1. **Link badges to session** - This can be used as an attendance system, simply send the trackId from client and the app will automatically grant the badge linked to the session based on the current time. This time management is done server side. 
2. **Allot individual badges** - You can grant individual badges too when a user performs a task, finds an easter egg, or clicks a link. Use the badgeId to make the call to grant individual badges. This badge may or may not be linked to a session.

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

### API Reference 🌐

#### Exchanging Access Token
```http
POST /api/auth/convert-token
```

| Parameter | Type | Value | Description |
| :--- | :--- | :--- | :---- |
| `grant_type` | `string` | `convert_token` | as it is |
| `client_id` | `string` | `<Django-Oauth-Client-ID>` | Copied previously |
| `backend` | `string` | `google-oauth2` | as it is |
| `token` | `string` | `<Google-Auth-Access-Token>` | Obtained when client side signin using Google Oauth2 API |

**example**:
```javascript
{
    "grant_type": "convert_token",
    "client_id": "hse8AgZkiHdVcGGtVRB3sbuW4w4DM46UA78fI50P",
    "backend": "google-oauth2",
    "token": "ya29.a0AfH6SMDnFAX_ZKMJNzv4CmVbQbWYCp6PLavVdfOzaJEGHjAaoOxN86UUXLyic_a1ZMJRqVJxd1t5IkGjdVPlnZxwWPJUrRF2TujZISkwDV2iFQtzsEfUMYsdcWt0hJ8Pk1wvNugf-QwZs0jUlg8rdgp_PYCcMyI_7R4"
}
```

**Response**
```javascript
{
    "access_token": "Jd4hNC3qjljlzTBMSkdf97x0iOy5Fu",
    "expires_in": 36000,
    "token_type": "Bearer",
    "scope": "read write",
    "refresh_token": "Fcp6VflwUrrX65gxJ0qKnfxgYa1Q6a"
}
```

Save the access_token at the client and use the access token in the header for each authorized request. 
**Note**
You will receive a new access_token EACH TIME you login on the client and send request to this API. Make sure to overwrite the access_token with the fresh one every time. Or use the refresh token to get a new token after expiration. Feel free to send a PR to this documentation explaining that. 

#### Marking Attendance in a session
```http
POST /api/session
```

Set this as the header of the request

```Authorization: Bearer <access-token>```

| Parameter | Type | Value | Description |
| :--- | :--- | :--- | :---- |
| `track` | `integer` | `<track-value>` | send the track number of session/default 1 |

**example**:
```javascript
{
    "track": 1
}
```

**Response**
```javascript
{
    "user": "kautukkundan@gmail.com",
    "success": true,
    "badgeEarned": false
}
```

```badgeEarned``` parameter will be True/False depending on 
1. Whether the session has an associated badge or not
2. Whether the person already has the same badge or not
This parameter can be used to show a popup notification/toast at the frontend.

#### Fetching Sessions of a user 
```http
GET /api/session
```

Set this as the header of the request

```Authorization: Bearer <access-token>```

**Response**
```javascript
{
    "sessions": [
        {
            "sessionId": "D01S01",
            "name": "Keynote on ML",
            "start": "2020-07-04T16:44:25+05:30",
            "end": "2020-07-05T16:44:26+05:30"
        }
    ],
    "uuid": "6179ea9a-363f-4d1f-a597-07715b612c2e"
}
```

```uuid``` is returned on every get call session/badges. This UUID can be used to anonymously fetch the public profile of the user.

#### Granting Individual Badges
```http
POST /api/badges
```

Set this as the header of the request

```Authorization: Bearer <access-token>```

| Parameter | Type | Value | Description |
| :--- | :--- | :--- | :---- |
| `badge` | `string` | `<badge-id>` | send badge ID |

**example**:
```javascript
{
    "badge":"secretBadge1"
}
```

**Response**
```javascript
{
    "user": "kautukkundan@gmail.com",
    "success": true,
    "badgeEarned": false,
    "badge": "secretBadge1"
}
```

This route can be used to grant badges which are not attached to any particular sessions but are present independently.
1. Easter Egg
2. Special Badges for exclusive users
etc

#### Fetching Badges of a user 
```http
GET /api/session
```

Set this as the header of the request

```Authorization: Bearer <access-token>```

**Response**
```javascript
{
    "badges": [
        {
            "badgeId": "D01S01badge",
            "name": "Watched ML Keynote",
            "image": "/media/badge/lAWQtaCV_400x400_pOV3u2h.jpg"
        },
        {
            "badgeId": "D01S02badge",
            "name": "ML Overlord!",
            "image": "/media/badge/lAWQtaCP_400x400_pOV3u2g.jpg"
        }
    ],
    "uuid": "6179ea9a-363f-4d1f-a597-07715b612c2e"
}
```

```uuid``` is returned on every get call session/badges. This UUID can be used to anonymously fetch the public profile of the user.

#### Fetching Badges/Session using Public profile 
```http
GET /api/session/collection/<uuid>

GET /api/badges/collection/<uuid>
```

No Auth needed

**Response**
```javascript
{
    "badges": [
        {
            "badgeId": "D01S01badge",
            "name": "Watched ML Keynote",
            "image": "/media/badge/lAWQtaCV_400x400_pOV3u2h.jpg"
        },
        {
            "badgeId": "D01S02badge",
            "name": "ML Overlord!",
            "image": "/media/badge/lAWQtaCP_400x400_pOV3u2g.jpg"
        }
    ],
    "email": "kau*****@gmail.com"
}
```

```email``` is returned in an obscured fashion. This link can be shared by the users on social media and people can visit this link to view the user's badges. 


### Deployement 📦
This application was deployed on DigitalOcean for use during our event. You can follow [this article](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04) for setup and deployments, this should work the same for any cloud service. 


### Known Issues and Notes 🐞
1. Each time a user logs in a new ```access_token``` and ```refresh_token``` is created in the database. They grow to a huge number and takes a lot of space. It's recommended to delete all the tokens from time to time.
2. If anyone has any solution to this issue (solution - Automatically delete old tokens when new tokens are created) please feel free to fix it and send a PR here. This app depends on [rest-framework-social-oauth2](https://github.com/RealmTeam/django-rest-framework-social-oauth2) for oauth2. 

3. HAVE LOTS OF FUN WHILE HOSTING YOUR NEXT eMEETUP!! ⭐️ this project if you like it :D 
4. Follow me on [twitter](https://twitter.com/kautukkundan) for more!
