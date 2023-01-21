# Social Media API

This API allows users to post messages and like other users' messages.

This API is build using

- Flask - For backend api mangament
- Postgres - For Database
- Hasura - For Graphql Support
- Docker

**Table of Contents**

- [Features](#Features)
- [Endpoints](#Endpoints)
- [Setup and run](#Setup-and-run)
  - [Run app in Linux](#Run-app-in-Linux)
  - [Run with Docker](#Run-with-docker)

## Features

- Post a new message
- View a list of all messages, with the most recent messages first
- Like a message by clicking a button
- View the total number of likes for each message

## Endpoints

1. `Post /messages` : Post a new message
   This endpoint allows users to post a new message. The request should include the following JSON data in the request body:

```
{
    "user_id": <user_id>,
    "text": <message>
}
```

2. `GET /messages` : Get list of all messages
   This endpoint allows users to view a list of all messages, with the most recent messages first.
3. `POST /messages/likes` : Like a message. The request should include the following JSON data in the request body:

```
{
    "message_id": <message_id>,
    "user_id": <user_id>
}
```

`message_id` can be obtained from endpoint `GET /messages`

4. `GET /messages/likes` : Get count of likes for the message. The request should include the following JSON data in the request body:

```
{
    "message_id": <message_id>
}
```

5. `DELETE /messages/likes` : Remove like of user for the message. The request should include the following JSON data in the request body:

```
{
    "message_id": <message_id>,
    "user_id": <user_id>
}
```

Both `message_id` and `user_id` should be valid for the given like.

## Setup and run

### Run app in Linux

The project runs on Python 3.

1. Create a virtual enviorntment:

```
python3 -m venv venv
```

2. Activate the virtual environment:

```
source venv/bin/activate
```

3. Install all the dependencies in `requirements.txt` file:

```
pip install -r requirements.txt
```

4. Set Up Postgres Database : Social
   - Using Hasura
     - Connect Database to ur hasura console
     - Goto Data -> SQL
     - Select Database
     - Copy and paste sql code from `social.sql` and run
     - Your Database is set....
   - Using psql terminal
     - Create Database 'social' using `sudo -u postgres psql createdb social`
     - use psql social < social.db
     - Your Database is set
5. Set Database URI as required in `app/config.py` file.
6. Set enviroment variable as required.

- For Production

```
export ENV='prod'
```

- For Development

```
export ENV='prod'
```

5. Run the app

```
 flask run
```

6. Navigate to http://localhost:5000 or the current server in which you are running(will be shown when app is running) in your browser.
7. When you are done using the app, deactivate the virtual environment:

```
deactivate
```

### Run with Docker
