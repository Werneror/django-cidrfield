from django.test import TestCase
from django.db.models import Model
from django.db import IntegrityError
from .models import IPNetworkField

import ipaddress


class DummyModel(Model):
    field = IPNetworkField()
    null_field = IPNetworkField(null=True)

    def __str__(self):
        return field.__str__()

    __repr__ = __str__


class IPNetworkFieldTests(TestCase):

    def test_ipv4_equal(self):
        DummyModel.objects.create(field='192.168.1.0/24')
        self.assertEqual(DummyModel.objects.filter(field='192.168.1.0/24').count(), 1)
        self.assertEqual(DummyModel.objects.filter(field='192.168.1.32').count(), 0)
        self.assertEqual(DummyModel.objects.filter(field='192.168.2.0/24').count(), 0)

    def test_ipv6_equal(self):
        DummyModel.objects.create(field='FEC0:0000:0000:0000:0000:0000:0000:0000/10')
        self.assertEqual(DummyModel.objects.filter(field='fec0::/10').count(), 1)
        self.assertEqual(DummyModel.objects.filter(field='fec0::1').count(), 0)
        self.assertEqual(DummyModel.objects.filter(field='2001:4860:4860::8888').count(), 0)

    def test_ipv4_in(self):
        DummyModel.objects.create(field='10.10.10.0/24')
        self.assertEqual(DummyModel.objects.filter(field__in='10.10.0.0/16').count(), 1)
        self.assertEqual(DummyModel.objects.filter(field__in='10.10.10.0/30').count(), 0)

    def test_ipv6_in(self):
        DummyModel.objects.create(field='fec4::/16')
        self.assertEqual(DummyModel.objects.filter(field__in='fec0::/10').count(), 1)
        self.assertEqual(DummyModel.objects.filter(field__in='fec0::1').count(), 0)

    def test_ipv4_contains(self):
        DummyModel.objects.create(field='10.20.10.0/24')
        self.assertEqual(DummyModel.objects.filter(field__contains='10.20.10.1').count(), 1)
        self.assertEqual(DummyModel.objects.filter(field__icontains='10.20.10.1').count(), 1)
        self.assertEqual(DummyModel.objects.filter(field__contains='10.30.10.1').count(), 0)
        self.assertEqual(DummyModel.objects.filter(field__icontains='10.30.10.1').count(), 0)

    def test_ipv6_contains(self):
        DummyModel.objects.create(field='fec8::/16')
        self.assertEqual(DummyModel.objects.filter(field__contains='fec8::1').count(), 1)
        self.assertEqual(DummyModel.objects.filter(field__icontains='fec8::1').count(), 1)
        self.assertEqual(DummyModel.objects.filter(field__contains='fec4::1').count(), 0)
        self.assertEqual(DummyModel.objects.filter(field__icontains='fec4::1').count(), 0)

    def test_required_values(self):
        with self.assertRaises(IntegrityError):
            # non-null field should require value
            DummyModel.objects.create()

    def test_null_values(self):
        # null field can be left empty
        DummyModel.objects.create(field='::1')

    def test_max_values(self):
        DummyModel.objects.create(field='ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff')
        DummyModel.objects.create(field='255.255.255.255')
