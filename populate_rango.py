import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page
import random as r

def populate():

    python_pages = [
        {'title': 'Official Python Tutorial',
        'url':'http://docs.python.org/3/tutorial/',
        'views': 0},
        {'title':'How to Think like a Computer Scientist',
        'url':'http://www.greenteapress.com/thinkpython/',
        'views': 0},
        {'title':'Learn Python in 10 Minutes',
        'url':'http://www.korokithakis.net/tutorials/python/', 
        'views': 0},]

    django_pages = [
        {'title':'Official Django Tutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/', 
        'veiws': 0},
        {'title':'Django Rocks',
        'url':'http://www.djangorocks.com/', 
        'veiws': 0},
        {'title':'How to Tango with Django',
        'url':'http://www.tangowithdjango.com/', 
        'veiws': 0},]

    other_pages = [
        {'title':'Bottle',
        'url':'http://bottlepy.org/docs/dev/',
        'views': 0},
        {'title':'Flask',
        'url':'http://flask.pocoo.org',
        'views': 0},]

    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16} }

    for cat, cat_data in cats.items():
        """
        if cat == "Python":
            c = add_cat(cat, 128, 64)
        elif cat == "Django":
            c = add_cat(cat, 64, 32)
        else:
           c = add_cat(cat, 32, 16) 
        """
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            p['views'] = r.randint(1, 100)
            add_page(c, p['title'], p['url'], p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title, views = views)[0]
    p.url=url
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name, views=0, likes=0)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()