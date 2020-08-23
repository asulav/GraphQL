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
django-admin startproject tutorial .
cd tutorial
django-admin startapp story
cd ..
```
```
# Migrate the default database
python manage.py migrate
```

```
# Create Super User
python manage.py createsuperuser --email admin@example.com --username admin
```
---------
> Inside ***stories/models.py***
```
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    twitter_account = models.CharField(max_length=50, null=True, blank=True)

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
---------
> Inside ***stories/serializers.py***
```
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'
```
> Inside ***stories/views.py***
```
from tutorial.story.models import Author, Story
from rest_framework import viewsets
from tutorial.story.serializers import AuthorSerializer, StorySerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class StoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Story.objects.all()
    serializer_class = StorySerializer
```
