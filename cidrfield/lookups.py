from django.db.models import Lookup


class IpContains(Lookup):
    lookup_name = 'contains'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = rhs_params + lhs_params
        return '%s like %s' % (rhs, lhs), params


class IpIn(Lookup):
    lookup_name = 'in'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return '%s like %s' % (lhs, rhs), params
