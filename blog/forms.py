from django import forms


class BlogForm(forms.Form):
    title = forms.CharField(label="Title", max_length=140, widget=forms.TextInput(
        attrs={'class': 'form-control bef bef-bg-moccasin bef-text-mystic', 'id': 'title', 'name': 'title', 'placeholder': 'Enter New blog title'}))
    sub_title = forms.CharField(label="Sub Title", max_length=140, widget=forms.TextInput(
        attrs={'class': 'form-control bef bef-bg-moccasin bef-text-mystic', 'id': 'sub_title', 'name': 'sub_title', 'placeholder': 'Enter New blog sub title'}))
    content = forms.CharField(label="Content", max_length=500, widget=forms.Textarea(
        attrs={'class': 'form-control bef bef-bg-moccasin bef-text-mystic', 'rows': '2', 'cols': '30', 'id': 'content', 'name': 'content', 'placeholder': 'Enter New blog content'}))
    image = forms.ImageField(label="Image", required=False, widget=forms.FileInput(
        attrs={'class': 'form-control bef bef-bg-moccasin bef-text-mystic', 'id': 'image', 'name': 'image'}))
