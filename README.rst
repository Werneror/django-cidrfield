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
    
    
	MyModel.objects.filter(ip_network='192.168.1.0/24')
	MyModel.objects.filter(ip_network__contains='192.168.1.1')
	MyModel.objects.filter(ip_network__in='192.168.0.0/16')
	MyModel.objects.filter(ip_network__in=['192.168.0.0/16', '10.10.0.0/16'])


If you use `DjangoQL <https://pypi.org/project/djangoql/>`_, you can use ``CIDRQLSchema`` like the following::
    
    
	from django.contrib import admin
	from djangoql.admin import DjangoQLSearchMixin
	from cidrfield.schemas import CIDRQLSchema
	from .models import MyModel
	
	
	@admin.register(MyModel)
	class MyModelAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
	    list_display = ['ip_network']
	    search_fields = ('ip_network', )
	    djangoql_schema = CIDRQLSchema


Changelog
---------

0.2.1
>>>>>

- Fix IPv6 with integers less than 2**32 being detected as IPv4.

0.2.0
>>>>>

- Add support for Djangoql.
- Fixed the bug about ``__in`` query not supporting array.
