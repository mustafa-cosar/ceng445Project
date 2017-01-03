from django import forms


class LoadForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LoadForm, self).__init__(*args, **kwargs)
        self.fields['availableComponents'] = forms.ChoiceField(choices=kwargs.get('choices', []))

    availableComponents = forms.ChoiceField()
