from django import forms


class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField(label='Browse for your ECR file...')
    # file.css_classes('form-control')
