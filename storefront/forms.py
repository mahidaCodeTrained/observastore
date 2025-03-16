from django import forms
from .widgets import CustomClearableFileInput
from .models import StoreGoods, Category


class StoreForm(forms.ModelForm):

    class Meta:
        model = StoreGoods
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        visual_names = [(c.id, c.get_visual_name()) for c in categories]

        self.fields['category'].choices = visual_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0 form-control'
