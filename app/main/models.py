from django.db import models

# Create your models here.
class Academy(models.Model):
    name = models.CharField(max_length=100,default='Academy_Name')
    status = models.CharField(max_length=6,default='open')
    price = models.DecimalField(decimal_places=2,max_digits=5,blank=False)
    nos = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        dis = self.name + "-- Number of courts : "+str(self.nos)
        return dis

    class Meta:
        ordering = ['created']

    class Meta:
        db_table = "Academies"