from setuptools import setup, find_packages
 
version = '0.1.0'
 
LONG_DESCRIPTION = """
================================================================
django-staticfiles-mediafinder (Django StaticFiles Media Finder)
================================================================

Django (http://djangoproject.com ) as of version 1.3 will include
the django-staticfiles application as a contrib app. With this
change, also comes a backwards incompatble change, where the
sub directory an application could use is renamed from
media to static.

This app is meant to be a temporary solution to allow the media
sub directory to be used, until third party apps are updated
to reflect the new name.
"""
 
setup(
    name='django-staticfiles-mediafinder',
    version=version,
    description="django-staticfiles-mediafinder",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='staticfiles,django',
    author='Donald von Stufft',
    author_email='donald.stufft@gmail.com',
    url='https://github.com/dstufft/django-staticfiles-mediafinder',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
