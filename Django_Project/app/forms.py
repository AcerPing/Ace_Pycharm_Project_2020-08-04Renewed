from django.forms import ModelForm, TextInput
from datetime import date
from .models import Record,Category

class RecordForm(ModelForm):

    def __init__(self,user,*args,**kwargs):
        super().__init__(*args, **kwargs)
        by_user = Category.objects.filter(user=user) | Category.objects.filter(pk=39)
        self.fields['category'].queryset = by_user

    class Meta:
        model = Record
        fields = ['date', 'description', 'category', 'cash', 'balance_type'] #日期, 描述, 分類, 金額, 收支
        widgets = {
            'date':TextInput(
                attrs={
                    'id':'datepicker1',
                    'value': date.today().strftime('%Y-%m-%d')
                }
            )
        }