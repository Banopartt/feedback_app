from django import forms
from .models import Names
#class review_form(forms.Form):
    #user_name = forms.CharField(max_length=10, label="Your Name", error_messages={
       # 'required': "You have to fill the blanks",
        #'max_length': "Length should be in between 10 chars"
    #})
    #review_text = forms.CharField(widget=forms.Textarea, max_length=1000)
    #rating = forms.IntegerField(max_value=5, min_value=1)
    
class review_form(forms.ModelForm):
    class Meta:
        model = Names
        fields = "__all__"
        labels = {
            "name": "Your name",
            "review_text": "Your FeedBack"      
        }