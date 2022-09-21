import ipaddress
from djangoql.schema import DjangoQLSchema
from djangoql.schema import DjangoQLField
from djangoql.exceptions import DjangoQLSchemaError
from .models import IPNetworkField


class DjangoQLIPNetworkField(DjangoQLField):
    type = 'ip'
    value_types = [ipaddress.ip_network, ipaddress.ip_address]
    value_types_description = 'ip address or ip network'

    def validate(self, value):
        if not self.nullable and value is None:
            raise DjangoQLSchemaError(
                'Field %s is not nullable, '
                'can\'t compare it to None' % self.name
            )
        try:
            ipaddress.ip_network(value, strict=False)
        except ValueError:
            raise DjangoQLSchemaError('"{}" is not a valid IP address or IP network.'.format(value))

    def as_dict(self):
        return {
            'type': 'str',
            'nullable': self.nullable,
            'options': [],
        }


class CIDRQLSchema(DjangoQLSchema):

    def get_field_cls(self, field):
        if isinstance(field, IPNetworkField):
            return DjangoQLIPNetworkField
        else:
            return super().get_field_cls(field)
