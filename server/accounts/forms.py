from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from .models import AccountUser

class AccountUserLoginForm(AuthenticationForm):
    class Meta:
        model = AccountUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(AccountUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class AccountUserRegisterForm(UserCreationForm):
    class Meta:
        model = AccountUser
        fields = ('username', 'first_name', 'password', 'password2', 'email', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = 'HELP TEXT'

    #def clean_age(self):
    #    data = self.cleaned_data['age']
    #    if data < 18:
    #        raise forms.ValidationError('Вы слишком молоды')
    #    return data

class AccountUserEditForm(UserChangeForm):
    class Meta:
        model = AccountUser
        fields = ('username', 'first_name', 'email', 'age', 'avatar', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = 'HELP TEXT'
            #if field_name == 'password':
            #    field.widget = forms.HiddenInput()

    #def clean_age(self):
    #    data = self.cleaned_data['age']
    #    if data < 18:
    #        raise forms.ValidationError('Вы слишком молоды')
    #    return data