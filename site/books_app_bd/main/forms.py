from .models import Authors,Pub_house,Books
from django.forms import ModelForm,TextInput,NumberInput,DateInput,	ModelChoiceField

class AuthorsForm(ModelForm):
    class Meta:
        model=Authors
        fields=["name","surname","cit","birthday"]
        widgets={

            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя автора'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию автора'
            }),
            "cit": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите гражданство автора'
            }),

            "birthday": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату рождения автора'
            }),
        }

class Pub_houseForm(ModelForm):
    class Meta:
        model=Pub_house
        fields=["name","country"]
        widgets={
             "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название издательства'
            }),
            "country": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите страну'
            })}

class BooksForm(ModelForm):
    class Meta:
        model=Books

        id_a = ModelChoiceField(queryset=Authors.objects.all())
        id_ph = ModelChoiceField(queryset=Pub_house.objects.all())
        fields=["name","num_page","seria","id_a","id_ph"]
        widgets={
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название книги'
            }),
            "seria": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название серии книг'
            }),
            "num_page": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите колво страниц'
            })}


