from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
#importing product from the store app
# from store.models import Product
#these two apps are completely different apps, so importing shouldn't be done

# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    # product = models.ForeignKey(Product)

    # generic relations
    # type (product, video, article)
    # id

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey() # actual object that a tag is applied to