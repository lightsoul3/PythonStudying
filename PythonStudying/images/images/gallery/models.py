from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image
import sys

# Create your models here.
class Gallery(models.Model):
    name = models.CharField(verbose_name='Name', default='')
    type = models.CharField(verbose_name='Type', default='')
    image = models.ImageField(upload_to='gallery/', blank=True, verbose_name='Image')
    preview = models.ImageField(upload_to='gallery/preview/', blank=True, verbose_name='Preview')

    def save(self, **kwargs):
        output_size = (100, 100)
        output_thumb = BytesIO()

        img = Image.open(self.photo)
        img_name = self.photo.name.split('.')[0]

        if img.height > 100 or img.width > 100:
            img.preview(output_size)
            img.save(output_thumb,format='PNG',quality=90)

        self.preview = InMemoryUploadedFile(output_thumb, 'ImageField', f"{img_name}_preview.png", 'image/png', sys.getsizeof(output_thumb), None)

        super(Gallery, self).save()