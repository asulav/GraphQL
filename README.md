### DRF Example
```
# Create the project directory
mkdir tutorial
cd tutorial

# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install Django and Django REST framework into the virtual environment
pip install django
pip install djangorestframework

# Set up a new project with a single application
django-admin startproject tutorial .  # Note the trailing '.' character
cd tutorial
django-admin startapp story
cd ..
```
```
# Migrate the default database
python manage.py migrate
```
```
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    twitter_account = models.CharField(max_length=50, null=True, blank=True)

    DISPLAY_FIRST_LAST = 'first_last'
    DISPLAY_LAST_FIRST = 'last_first'

    def full_name(self, display_format: str) -> str:
        if display_format == self.DISPLAY_FIRST_LAST:
            return f'{self.first_name} {self.last_name}'
        return f'{self.last_name}, {self.first_name}'

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Story(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=255)
    published_date = models.DateField()
    author = models.ForeignKey(Author, related_name='stories', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title} ({self.published_date.year})'
```
