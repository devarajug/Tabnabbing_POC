from django import forms

class LoginForm(forms.Form):
    """Login form implementation"""

    username = forms.CharField(
        max_length = 120,
        required = False,
        widget = forms.TextInput(
            attrs = {
                'placeholder':'Enter Your Email Address'
            }
        )
    )

    password = forms.CharField(
        max_length = 120,
        required = False,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder' : 'Enter Your Password'
            }
        )
    )

    def clean_username(self):
        """Validation for username"""
        username = self.cleaned_data.get("username")
        if not username:
            raise forms.ValidationError("email_error")
        else:
            return username

    def clean_password(self):
        """Validation for Password"""
        password = self.cleaned_data.get("password")
        if not password:
            raise forms.ValidationError("password_error")
        else:
            return password
