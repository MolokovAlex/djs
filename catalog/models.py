from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Catalog(models.Model):
    title = models.CharField(max_length=150)
    name = models.CharField(max_length=150)           # наимнование компонента, например "транзистор", "винт М2x20 DIN912 A2"
    amount = models.IntegerField()                       # количество на складе в единицах измерения
    code_unit = models.IntegerField()                   # код единицы измерения, например: "шт",  "комлект", "л" и т.д.
    unit = models.CharField(max_length=10)
    min_rezerve = models.IntegerField()                  # минимальный остаток на складе в единицах измерения
    store = models.CharField(max_length=150)         # где храниться компоенент
    articul_1C = models.CharField(max_length=150)                   # артикул компонента по базе 1С
    code_1C = models.IntegerField()                      # код по базе 1С
    name_1C = models.CharField(max_length=150)                      # наименование по базе 1С
    id_code_parent = models.IntegerField()               # служебное поле - id_code_item родителя(группы) компонента
    id_code_lvl = models.IntegerField()                   # служебное поле - буквенный код уровня вложенности родителя(группы) (поле только для группы)
    create_at  =models.DateTimeField()
    update_at = models.DateTimeField()
    photo = models.ImageField(upload_to='photos/')
    is_publ = models.BooleanField(default=True)
    comments = models.TextField(blank=True)                      # комментарии к компоненту
                  
    
    

