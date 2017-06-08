from django.db import models
from django.forms import ModelForm



# Create your models here.
class Map(models.Model):
    location = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=13,decimal_places=10,null=True)
    longitude = models.DecimalField(max_digits=13,decimal_places=10,null=True)
    def __str__(self):
        return self.location


class Tag(models.Model):
    tagName = models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.tagName

class User(models.Model):
    account = models.CharField(max_length=20)
    psw = models.CharField(max_length=30)
    name = models.CharField(max_length=20)

class Diary(models.Model):
    title = models.CharField(max_length=30, blank=False)
    date = models.DateField()
    content = models.CharField(max_length=1000,blank=True)
    weather = models.CharField(max_length=30)
    location = models.ForeignKey(Map,blank=True,null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:  # 排序用
        ordering = ['date']

class Media(models.Model):
    title = models.CharField(max_length=20)
    userId = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    img = models.FileField(upload_to = 'image/')
    diary = models.ForeignKey(Diary,on_delete=models.CASCADE,default=0)
    def __str__(self):
        return self.userId+'_'+str(self.id)
    def type(self):
        import os
        name,ext = os.path.splitext(self.img.name)
        if ext =='.jpg' or ext =='.jpeg' or ext == '.png' or ext=='.PNG':
            return 'img'
        elif ext == '.mp3':
            return 'music'
        return 'video'
    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.img.storage, self.img.path
        # Delete the model before the file
        super(Media, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)



# Forms
class DiaryForm(ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'date','content']

class MediaForm(ModelForm):
    class Meta:
        model = Media
        fields = ['title', 'userId', 'description', 'img']

