from django import forms
from .models import Cliente
from apps.venta.models import Factura

import datetime


class FacturaForm(forms.ModelForm):

    date = forms.DateField()

    class Meta:
        model = Factura
        fields = ['fecha_emision']

    def __init__(self, *args, **kwargs):
        super(FacturaForm, self).__init__(*args, **kwargs)
        today = datetime.date.today()

        self.fields["fecha_emision"].initial = format(today, '%Y-%m-%d')
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class ClienteModalForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['identificacion_tipo', 'activo', 'nombre', 'identificacion',
                  'obligado_contabilidad', 'direccion', 'telefono', 'celular', 'email']
        labels = {
            'identificacion_tipo': 'Tipo de Identificación',
            # 'usuario_creador': 'Creado por',
            # 'cliente_id': 'Tipo de Cliente',
            'activo': 'Activo?',
            'nombre': 'Apellidos y Nombres',
            'identificacion': 'Identificación',
            'obligado_contabilidad': 'Obligado a llevar contabilidad?',
            # 'codigo_contribuyente_especial': 'Código contribuyente especial',
            # 'es_rise': '¿Es RISE?',
            # 'es_cliente': '¿Es Cliente?',
            # 'es_sujeto_retenido': '¿Es sujeto retenido?',
            # 'es_transportista': '¿Es transportista?',
            # 'es_destinatario': '¿Es destinatario?',
            # 'placa': 'Número de placa',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            # 'extension': 'Extensión',
            'celular': 'Teléfono Celular',
            'email': 'Correo electrónico'
        }

        widgets = {
            'identificacion_tipo': forms.Select(attrs={'class': 'form-control'}),
            # 'usuario_creador': forms.Select(attrs={'class':'form-control'}),
            # 'cliente_id': forms.TextInput(attrs={'class':'form-control'}),
            'activo': forms.CheckboxInput(),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'identificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'obligado_contabilidad': forms.CheckboxInput(),
            # 'codigo_contribuyente_especial': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Código Contribuyente'}),
            # 'es_rise': forms.CheckboxInput(),
            # 'es_cliente': forms.CheckboxInput(),
            # 'es_sujeto_retenido': forms.CheckboxInput(),
            # 'es_transportista': forms.CheckboxInput(),
            # 'es_destinatario': forms.CheckboxInput(),
            # 'placa': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            # 'extension': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nombre@example.com'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean(self):
        try:
            sc = Cliente.objects.get(
                identificacion=self.cleaned_data["identificacion"].upper()
            )

            if not self.instance.pk:
                print("El registro ya existe")
                raise forms.ValidationError("El registro ya existe")
            elif self.instance.pk != sc.pk:
                print("Cambio no permitido")
                raise forms.ValidationError("Cambio no permitido")
        except Cliente.DoesNotExist:
            pass
        return self.cleaned_data
