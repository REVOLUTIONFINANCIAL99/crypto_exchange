from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Definir el modelo de usuario personalizado
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    # Campos adicionales para el formulario
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # Los campos que se incluyen en el formulario

    def clean_email(self):
        # Validación de correo electrónico único
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email

    def clean_username(self):
        # Validación de nombre de usuario único
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso.")
        return username
