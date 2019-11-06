.. -*- restructuredtext -*-

django-cidrfield
================

``cidrfield`` provides a model field for 
`django <https://www.djangoproject.com>`_
that allows the storage of an ip network on the db side by using ``ipaddress`` 
to handle conversion to an ``ipaddress.ip_network`` instance (or ``None``) 
on the python side. It supports the use of ``__contains`` and ``__in`` 
to query the IP network that contain and belong to.



Installation
------------

Add this to your django project by installing with ``pip``: ::
    
    pip install django-cidrfield



Usage
-----

In your models, do something like the following: ::
    
	from django.db import models
	from cidrfield.models import IPNetworkField

	class MyModel(models.Model):

	    # the regular params should work well enough here
	    ip_network = IPNetworkField()
	    # ... and so on


Then you can store a ip network like the following::
    
    
	MyModel(ip_network='192.168.1.0/24').save()


And you can query a ip network like the following::
    
    
	MyModel.objects.filter(ip_network__contains='192.168.1.1')
	MyModel.objects.filter(ip_network__in='192.168.0.0/16')

