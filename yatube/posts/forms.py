from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')

    def clean_text(self):
        data = self.cleaned_data['text']
        if data.split() == '':
            raise forms.ValidationError('Обязательное для заполнения поле')
        return data
