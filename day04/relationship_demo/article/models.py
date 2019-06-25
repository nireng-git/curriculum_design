from django.db import models

# Create your models here
class Category(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=20)
    articles = models.ManyToManyField("Article",related_name="tag")

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey("Category",on_delete=models.CASCADE,null=True,related_name="articles")
    author = models.ForeignKey("frontuser.FrontUser",on_delete=models.CASCADE,null=True)

    def __str__(self):
        return "<Article:(id:%s,title:%s)>" % (self.id,self.title)

