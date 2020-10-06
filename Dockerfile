#Not using pipenv as docker itself is a container
#username, email and password is hardcoded here. Make sure you chnage this before deploy and to .env/GitHub secrets or any secure way
FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN python manage.py collectstatic
RUN python manage.py migrate
RUN python manage.py makemigrations
RUN python manage.py migrate --run-syncdb
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin-badge', 'admin@example.com', 'passwordbadge#100')" | python manage.py shell
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 