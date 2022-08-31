from django.db import models
class TimespamModel(models.Model):
        created_at = models.DateTimeField(auto_now_add=True) 
        updated_at = models.DateTimeField(auto_now=True) 

        class Meta:
            abstract = True


class Post(TimespamModel):

    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title