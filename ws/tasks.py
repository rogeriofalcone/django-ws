from ws.celerytask import BPMTask
from ws import forms

class AddForm(forms.BPMTaskForm):
    a = forms.IntegerField(label="First number",
                           initial=2,
                           help_text="Must be a integer number",
                           max_value=999,
                           min_value=0)
    b = forms.IntegerField(label="Second number",
                           initial=2,
                           help_text="Must be a integer number",
                           max_value=999,
                           min_value=0)

class add(BPMTask):
    form = AddForm
    def run(self, workflow_task, a, b):
        return a + b


class dummy(BPMTask):
    form = forms.BPMTaskForm
    def run(self, workflow_task):
        return ''
