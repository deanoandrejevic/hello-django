from django.db import models

# Create your models here.
<<<<<<< HEAD


=======
>>>>>>> dcd57c3c14521a21b06f0666fe572aa84a7c56ab
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
<<<<<<< HEAD
        return self.name
=======
        return self.name
>>>>>>> dcd57c3c14521a21b06f0666fe572aa84a7c56ab
