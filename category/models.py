from django.db import models
# Create your models here.

class CategoryFirst(models.Model):
	name = models.CharField(max_length=255)

	class Meta:
		db_table = 'ecommerce_category_first'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['data'] = CategoryFirst.objects.all()
		return context




class CategorySecond(models.Model):
	parent = models.ForeignKey(
			CategoryFirst,
			on_delete=models.CASCADE
	)
	name = models.CharField(max_length=255)

	class Meta:
		db_table = 'ecommerce_category_second'



class CategoryThird(models.Model):
	parent = models.ForeignKey(
			CategorySecond,
			on_delete=models.CASCADE
	)
	name = models.CharField(max_length=255)

	class Meta:
		db_table = 'ecommerce_category_third'