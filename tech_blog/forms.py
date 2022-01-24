from allauth.account.forms import LoginForm
from wagtailcaptcha.models import WagtailCaptchaEmailForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

# adding the recaptcha field for login
class CapLoginForm(LoginForm):

    captcha = ReCaptchaField(
    widget=ReCaptchaV2Checkbox(
        attrs={'data-theme': 'light', 'data-size': 'normal',  },),
    )
    