from django.contrib.auth.forms import AuthenticationForm

from .models import AccountUser

class AccountUserLoginForm(AuthenticationForm):
    class Meta:
        model = AccountUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(AccountUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

