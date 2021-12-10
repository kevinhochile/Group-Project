from django.db import models

# Create your models here.


class Order(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=13, blank=True)
    order_Description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='photos')

    class Meta:
        db_table = "Order"

    def __str__(self):
        return(self.full_name)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def save(self):
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        super(Order, self).save()
