from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from django.contrib.auth.models import User




class Dossier(models.Model):
	name = models.CharField(max_length=100, verbose_name='Имя')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to='media', blank=True, verbose_name='Фото')
	description = models.TextField(null=True, blank=True, verbose_name='Описание')
	tag = TaggableManager()
	urls = models.SlugField(null=True)



	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Объект'
		verbose_name = 'Объект'
		ordering = ['name']