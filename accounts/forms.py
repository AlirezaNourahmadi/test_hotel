from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import Guest

class GuestRegistrationForm(UserCreationForm):
    class Meta:
        model = Guest
        fields = ['username', 'email', 'phone_number', 'address', 'password1', 'password2']
        labels = {
            'username': _('نام کاربری'),
            'email': _('ایمیل'),
            'phone_number': _('شماره تماس'),
            'address': _('آدرس'),
            'password1': _('رمز عبور'),
            'password2': _('تأیید رمز عبور'),
        }
        help_texts = {
            'username': _('لطفاً یک نام کاربری منحصربه‌فرد وارد کنید.'),
            'password1': _('رمز عبور باید حداقل شامل ۸ کاراکتر باشد و ترکیبی از حروف و اعداد باشد.'),
            'password2': _('رمز عبور را مجدداً وارد کنید تا از درستی آن اطمینان حاصل شود.'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = _('رمز عبور')
        self.fields['password2'].label = _('تأیید رمز عبور')
        self.fields['password1'].help_text = _('رمز عبور باید حداقل شامل ۸ کاراکتر باشد و ترکیبی از حروف و اعداد باشد.')
        self.fields['password2'].help_text = _('رمز عبور را مجدداً وارد کنید تا از درستی آن اطمینان حاصل شود.')
class PersianAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "نام کاربری"
        self.fields['password'].label = "رمز عبور"
        