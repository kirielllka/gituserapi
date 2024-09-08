from django import forms # Импортируем формы Django

class NameArticleForm(forms.Form):
    name = forms.CharField(label='Логин пользователя гитхаб')