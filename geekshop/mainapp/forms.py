from django.forms import ModelForm
from mainapp.models import Product, ProductsCategory

class CategoryCreationForm(ModelForm):
    class Meta:
        model = ProductsCategory
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

class CategoryEditForm(ModelForm):
    class Meta:
        model = ProductsCategory
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''