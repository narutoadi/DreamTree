from django.db import models

# Create your models here.
# pushing with office git
class Dream(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000, null=True)
    weight = models.FloatField()
    duration = models.DurationField()
    deadline = models.DateField()
    created = models.DateTimeField(auto_now=True)

class DreamFiles(models.Model):
    dream = models.ForeignKey(Dream,on_delete=models.CASCADE)
    file = models.FileField(upload_to='dreamFiles/')

class DreamHierarchy(models.Model):
    child = models.ForeignKey(Dream,on_delete=models.CASCADE,related_name='child_dream')
    parent = models.ForeignKey(Dream,on_delete=models.CASCADE,related_name='parent_dream')

class DreamDependency(models.Model):
    dream = models.ForeignKey(Dream,on_delete=models.CASCADE,related_name='the_dependent')
    dependency = models.ForeignKey(Dream,on_delete=models.CASCADE,related_name='the_dependency')

class DreamProgress(models.Model):
    dream = models.ForeignKey(Dream,on_delete=models.CASCADE)
    startDate = models.DateTimeField(auto_now=True)
    endDate = models.DateTimeField()
