from django import forms


class NewGameForm(forms.Form):
    title = forms.CharField(label="Game title", max_length=256,
                            initial="Untitled game")
    iterations = forms.IntegerField(label="Iterations (set this to 0 to keep "
                                          "it running until you end the game)",
                                    initial=10, min_value=0)
    text = forms.CharField(label="Text", widget=forms.Textarea, min_length=10)


class PostTextForm(forms.Form):
    text = forms.CharField(label="Text", widget=forms.Textarea, min_length=10)
