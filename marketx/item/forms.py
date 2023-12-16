from django import forms
from .models import Items

INPUT_CLASSES= 'w-full py-4 px-6 m-3 rounded-xl border border-black-solid'
class NewItemForm(forms.ModelForm):
   class Meta:
      model=Items
      fields=('category','name','description','price','image',)
      widgets={
         'category':forms.Select(attrs=
                                 {
                                    'class': INPUT_CLASSES
                                 }),
         'name':forms.TextInput(attrs=
                                 {
                                    'class': INPUT_CLASSES
                                 }),
         'description':forms.Textarea(attrs=
                                 {
                                    'class': INPUT_CLASSES
                                 }),
         'price':forms.TextInput(attrs=
                                 {
                                    'class': INPUT_CLASSES
                                 }),
         'image':forms.FileInput(attrs=
                                 {
                                    'class': INPUT_CLASSES
                                 })
      }
      
class EditItemForm(forms.ModelForm):
   class Meta:
      model=Items
      fields=('name','description','price','image','is_sold',)
      widgets={
         'name':forms.TextInput(attrs=
                                 {
                                    'class': INPUT_CLASSES
                                 }),
         'description':forms.Textarea(attrs=
                                 {
                                    'class': INPUT_CLASSES
                                 }),
         'price':forms.TextInput(attrs=
                                 {
                                    'class': INPUT_CLASSES
                                 }),
         'image':forms.FileInput(attrs=
                                 {
                                    'class': INPUT_CLASSES
                                 })
      }
      