from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe


# Create your models here.

class Cars(models.Model):
    manufacturer = models.CharField(max_length=100)
    description = RichTextField()
    published_date = models.DateTimeField(auto_now_add=True,)
    updated_date = models.DateTimeField(auto_now=True,)
    slug = models.SlugField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'car manufacturer'
        verbose_name_plural = "cars"

    def __str__(self):
        return self.manufacturer
    

class CarForms(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'form'
        verbose_name_plural = 'Car Forms'

    def __str__(self):
        return self.name


class CarSeries(models.Model):
    model = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='models', verbose_name= 'Manufacturer')
    serie = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    modelnumber = models.CharField(max_length=100, verbose_name='Car Complect')
    type = models.ManyToManyField(CarForms, related_name='formalar', null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    active = models.BooleanField(null=True,blank=True,)
    
    
    class Meta:
        verbose_name = 'car data'
        verbose_name_plural = "car series"
    
    def __str__(self):
        return f'{self.model} - {self.serie} - {self.modelnumber} - {self.year}'
    
    @property
    def how_many_comments(self):
        comment_count = self.modelnum.count()
        return comment_count
    
    @property
    def image_of_car(self):
        if self.image:
            return mark_safe(f"<img src={self.image.url} width=400 height=300></img>")
        return mark_safe(f"{self.model} {self.serie} {self.modelnumber} has not got an image")


class CarSeriesComments(models.Model):
    modelnumbers = models.ForeignKey(CarSeries, on_delete=models.CASCADE, related_name='modelnum', verbose_name='Car Model')
    comment = models.TextField()
    active = models.BooleanField(default=True)
    add_date = models.DateField(auto_now_add=True,)

    

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
    
    def __str__(self):
        return f'{self.modelnumbers.model} - {self.modelnumbers.serie} - {self.modelnumbers.modelnumber} - {self.modelnumbers.year}  |   Comment: {self.comment}'


