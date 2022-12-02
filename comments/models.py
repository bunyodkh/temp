from django.db import models



class Commment(models.Model):
    text = models.TextField(max_length=500, null=False, blank=False)
    
    created = models.DateTime()
    updated = models.DateTime()


    class Meta:
        ordering = ['-created']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    
    def __str__(self):
        return f'{self.author} - {self.created}' 

    