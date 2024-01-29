from django import forms


class MessageForm(forms.Form):
    content = forms.CharField(label="Content", max_length=500, widget=forms.Textarea(
        attrs={'class': 'form-control bef bef-bg-moccasin bef-text-mystic', 'rows': '2', 'cols': '30', 'id': 'content', 'name': 'content', 'placeholder': 'Enter New message content'}))
