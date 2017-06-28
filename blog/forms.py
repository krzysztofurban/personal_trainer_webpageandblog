from django import forms
from blog.models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, label="Twoje imię", required=True)
    email = forms.EmailField(label="Twój e-mail", required=True)
    to = forms.EmailField(required=True, label="E-mail odbiorcy")
    comments = forms.CharField(required=False, max_length=25, label="Wiadomość")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'name', 'email', 'body'}
        labels = {
            "name": "Imię:",
            "email": "E-mail:",
            "body": "Komentarz:",
        }
