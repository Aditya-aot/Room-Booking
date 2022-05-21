from faulthandler import disable
from django import forms
from django.forms import ModelForm
from .models import room_book , user_book



class ChatForm(ModelForm):
    a101 = forms.RadioSelect()

    class Meta:
        model = room_book
        fields = [
            'a101' ,
            'a102' ,
            'a103' ,
            'a104' ,
            'a105' ,
            'a106' ,
            'a107' ,
            'a108' ,
            # 'a102'
 ]

class ChatForm2(ModelForm):
    book = forms.RadioSelect()
    # book2 = forms.CheckboxInput(user_book.objects(40)) 
    
    class Meta:
        model = user_book
        fields = [
            'book' ,

 ]



# room_book object (40)
