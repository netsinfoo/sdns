import django_tables2 as tables
from django_tables2.utils import Accessor
from utilities.tables import BaseTable, ToggleColumn

from sdns.models import Register


class RegisterTable(BaseTable):
    pk = ToggleColumn()
    ip = tables.LinkColumn(
        viewname='plugins:sdns:register_edit',
        args=[Accessor('pk')]
    )

    class Meta(BaseTable.Meta):
        model = Register
        fields = (
            'pk',
            'ip',
            'host',
            'domain',
        )
