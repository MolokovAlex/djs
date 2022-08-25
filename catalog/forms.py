from django import forms
from .models import Seller


class AdvertForm(forms.Form):
    title = forms.CharField(max_length=150, label='Наименование', widget=forms.TextInput(attrs={"class": "form-control"}))
    name = forms.CharField(max_length=150, label='Название', required=False, widget=forms.TextInput(attrs={"class": "form-control"}) )
    # price = models.IntegerField( verbose_name='Цена', blank=True )
    # amount = models.IntegerField()                       # количество на складеу продавца в единицах измерения
    # code_unit = models.IntegerField()                   # код единицы измерения, например: "шт",  "комлект", "л" и т.д.
    # unit = models.CharField(max_length=10)
    # min_rezerve = models.IntegerField()                  # минимальный остаток на складе в единицах измерения
    # store = models.CharField(max_length=150)         # где храниться компоенент
    # articul_1C = models.CharField(max_length=150)                   # артикул компонента по базе 1С
    # code_1C = models.IntegerField()                      # код по базе 1С
    # name_1C = models.CharField(max_length=150)                      # наименование по базе 1С
    # id_code_parent = models.IntegerField()               # служебное поле - id_code_item родителя(группы) компонента
    # id_code_lvl = models.IntegerField()                   # служебное поле - буквенный код уровня вложенности родителя(группы) (поле только для группы)
    # create_at  =models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации' )
    # update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено' )
    seller = forms.ModelChoiceField(queryset=Seller.objects.all(), label='Продавец', empty_label=None, widget=forms.Select(attrs={"class": "form-control"}))
    # photo = models.ImageField(upload_to='photos/', blank=True, verbose_name='Фото' )
    is_publ = forms.BooleanField( label='Опубликовано', initial=True)
    comments = forms.CharField( label='Комментарии', required=False, widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}) )                      # комментарии к товару