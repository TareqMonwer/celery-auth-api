## How to run the project:
+ clone the repo and `cd` into the codebase.
+ create and activate virtual-environment
+ install dependencies using `pip install -r requirements.txt --no-cache-dir`
+ create `.env` file & provide information as shown in `.env.example`
+ run `python manage.py makemigrations` if needed.
+ run `python manage.py migrate`
+ start redis-server using `redis-server --port 6360`.
+ run celery using: `celery -A config worker -l info`
+ run django server: `python manage.py runserver`

You're all set to play with the project.

## Highlights:
+ authentication with allauth
+ SEND CONFIRMATION EMAIL WITH CELERY.
+ Use CustomEmailBackend
