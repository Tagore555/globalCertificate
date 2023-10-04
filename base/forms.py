from django.forms import ModelForm
#from .models import Details

class DetailsForm(ModelForm):
    class Meta:
        model = Details
        fields = '__all__'





class FullCollegeForm(ModelForm):
    class Meta:
        model = FullCollege
        fields = '__all__'