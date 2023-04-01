from django import forms

# Crearemos los modelos de los Blogs.

class BlogForm (forms.Form):

    title = forms.CharField(max_length=100)
    subtitle = forms.CharField(max_length=200)
    body = forms.CharField()
    author = forms.CharField(max_length=50)

