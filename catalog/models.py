# from distutils.command.upload import upload
# from pyexpat import model
# from tabnanny import verbose
from django.db import models
from django.urls import reverse

# Create your models here.

class Catalog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    name = models.CharField(max_length=150, verbose_name='Название' ) #, help_text="Введите наименование товара")           # наимнование товара
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
    create_at  =models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации' )
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено' )
    seller = models.ForeignKey('Seller', on_delete=models.PROTECT, null=True, verbose_name='Продавец')
    photo = models.ImageField(upload_to='photos/', blank=True, verbose_name='Фото' )
    is_publ = models.BooleanField(default=True, verbose_name='Опубликовано' )
    comments = models.TextField(blank=True, verbose_name='Комментарии' )                      # комментарии к товару
                  
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-create_at']
    
    def get_absolute_url(self):
        return reverse('name_path_view_advert', kwargs={"advert_id": self.pk})

class Seller(models.Model):
#     #seller_id = models.IntegerField(blank=True)       # сделает автоматически
    seller_name = models.CharField(max_length=150, db_index=True, verbose_name='Имя Продавца')
#     seller_phone = models.CharField(max_length=150)
#     seller_email = models.EmailField(blank=True)

    class Meta:
            verbose_name = 'Продавец'
            verbose_name_plural = 'Продавцы'
            ordering = ['seller_name'] 

    def __str__(self) -> str:
        return self.seller_name

    def get_absolute_url(self):
        return reverse('name_path_seller', kwargs={"seller_id": self.pk})

# class Genre(models.Model):
#     name = model.CharField(max_length=150)
    
#     def __str__(self) -> str:
#         return self.name

