from django.forms import Form, ModelForm, CharField, PasswordInput
from .models import Diario, Usuario, Noticia, Autor


class DiarioForm(ModelForm):
    class Meta:
        model = Diario
        fields = '__all__'


class UsuarioForm(ModelForm):
    contrasena = CharField(widget=PasswordInput)

    class Meta:
        model = Usuario
        fields = '__all__'


class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'


class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'


class SearchForm(Form):
    clave = CharField(max_length=50)
