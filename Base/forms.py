# from django.forms import ModelForm
# from .models import Contact

# class ContactForm(ModelForm):
#     class Meta:
#         model = Contact
#         fields = ['name', 'text']




from django.forms import ModelForm
from django import forms
from .models import Contact


from django import forms  # type: ignore[reportMissingModuleSource]
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-900 rounded-lg p-3 mb-[15px]' ,
                
            }),

            'description': forms.Textarea(attrs={
                'class': 'w-full border border-gray-900  rounded-lg p-3 h-40 mb-[15px]',
            }),

            'narxi': forms.TextInput(attrs={
                'class': ' border border-gray-900  rounded-lg mb-[15px] p-[5px] w-[200px] ',
            }),

            'skidkasi': forms.TextInput(attrs={
                'class': ' border border-gray-900  rounded-lg mb-[15px] p-[5px] w-[200px] ',
            })
            
        }
        


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'text']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-3',
                'placeholder': 'Ismingizni kiriting'
            }),

            'text': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-3 h-40',
                'placeholder': 'Xabaringizni yozing'
            })
        }

