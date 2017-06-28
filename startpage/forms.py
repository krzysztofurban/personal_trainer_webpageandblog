from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label="Imię:")
    contact_email = forms.EmailField(required=True, label="E-mail:")
    contact_number = forms.CharField(max_length=12, label="Numer telefonu:")
    content = forms.CharField(required=False, widget=forms.Textarea, label="Wiadomość:")