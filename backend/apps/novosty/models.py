from django.db import models

# Create your models here.
#NOVOSTY MODELS

class Category(models.Model):
    name = models.CharField("Тема", max_length=50,unique=True)
    slug = models.SlugField("Слаг",max_length=60,unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories",
    )
    name = models.CharField("Тема", max_length=70, unique=True)
    slug = models.SlugField("Слаг", max_length=80, unique=True)

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        ordering = ['category', 'name']

    def __str__(self):
        return self.name


class Novosty(models.Model):
    name = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")
    image = models.ImageField("Фото", upload_to="novosty_images/")
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="novosti",
    )
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.PROTECT,
        related_name="novosti",
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Новост"
        verbose_name_plural = "Новости"
        ordering = ['-created']

    def __str__(self):
        return self.name


class Review(models.Model):
    novosty = models.ForeignKey(Novosty,on_delete=models.CASCADE, related_name="reviews")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    text = models.TextField("Отзыв")
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField("Активный", default=True)


    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created']

    def __str__(self):
        return f'{self.id}'
