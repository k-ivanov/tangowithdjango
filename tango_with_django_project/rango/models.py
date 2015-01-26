from django.db import models
from django.db.models import Model
from django.template.defaultfilters import slugify
# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length = 128, unique = True)
	views = models.IntegerField(default = 0)
	likes = models.IntegerField(default = 0)
	slug = models.SlugField(unique=True)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)
	def __unicode__(self):
		return self.name

class Page(models.Model):
	#CharField stores character data
	#URLField stores URL resources
	#IntegerField stores integers
	#ForeignKey,a field type that allows us to create a one-to-many relationship

	category = models.ForeignKey(Category)
	title = models.CharField(max_length = 128) 
	url = models.URLField() 
	views = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.title