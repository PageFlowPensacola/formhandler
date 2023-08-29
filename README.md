# Simple form forwarder

`flask run` or `./runme.sh`

[Sendgrid resource](https://sendgrid.com/blog/sending-emails-from-python-flask-applications-with-twilio-sendgrid/)
[Heroku resource](https://stackabuse.com/deploying-a-flask-application-to-heroku)

There is also `flask shell`

```
export FLASK_ENV=development
export FLASK_DEBUG=1
```

```
heroku config:set SENDGRID_API_KEY
heroku config:set MAIL_DEFAULT_SENDER
git push heroku main
```
