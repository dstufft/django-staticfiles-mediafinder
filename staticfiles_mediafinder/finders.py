from django.contrib.staticfiles.storage import AppStaticStorage as _DjangoAppStaticStorage
from django.contrib.staticfiles.finders import AppDirectoriesFinder as _DjangoAppDirectoriesFinder

class AppStaticStorage(_DjangoAppStaticStorage):
    source_dir = 'static'

class AppDirectoriesFinder(_DjangoAppDirectoriesFinder):
    storage_class = AppStaticStorage
