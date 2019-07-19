from django.db import models

# Create your models here.

class Host(models.Model):

    host = models.URLField()
    typed = models.CharField(max_length=255)

    def __str__(self):
        return self.host

class Document(models.Model):

    url = models.CharField(max_length=1000)
    method = models.CharField(max_length=25)
    params = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    query = models.TextField(null=True, blank=True)
    headers = models.TextField(null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    typed = models.ForeignKey(Host,on_delete=models.DO_NOTHING,related_name='doc',db_constraint=False)

    def __str__(self):
        return self.description



