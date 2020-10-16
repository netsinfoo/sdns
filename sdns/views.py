from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.views.generic import View
from utilities.views import BulkDeleteView, ObjectEditView, ObjectListView, ObjectDeleteView



from .filters import RegisterFilter
from .forms import RegisterFilterForm, RegisterForm
from .models import  Register
from .tables import RegisterTable
# Create your views here.
class RegisterListView(PermissionRequiredMixin, ObjectListView):
    permission_required = 'sdns.view_register'
    queryset = Register.objects.all()
    filterset = RegisterFilter
    filterset_form = RegisterFilterForm
    table = RegisterTable
    template_name = 'sdns/register_list.html'

class RegisterCreateView(PermissionRequiredMixin, ObjectEditView):
    permission_required = 'sdns.add_register'
    model = Register
    queryset = Register.objects.all()
    model_form =  RegisterForm
    template_name = 'sdns/register_edit.html'
    default_return_url = 'plugins:sdns:register_list'

class RegisterBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    permission_required = 'sdns.delete_register'
    queryset = Register.objects.filter()
    table = RegisterTable
    default_return_url = 'plugins:sdns:register_list'

class RegisterView(View):
    """Single virtual circuits view, identified by ID."""

    def get(self, request, pk):
        vc = get_object_or_404(VirtualCircuit.objects.filter(vcid=pk))
        vlan_ids = VirtualCircuitVLAN.objects.filter(virtual_circuit=vc).values_list('vlan_id', flat=True)
        vlans = [VLAN.objects.get(pk=vid) for vid in vlan_ids]

        return render(request, 'netbox_virtual_circuit_plugin/virtual_circuit.html', {
            'virtual_circuit': vc,
            'vlans': vlans,
        })

class RegisterEditView(RegisterCreateView):
    permission_required = 'sdns.change_sdns'

class RegisterDeleteView(PermissionRequiredMixin, ObjectDeleteView):
    permission_required = 'sdns.delete_register'
    model = Register
    default_return_url = 'plugins:sdns:register_list'

