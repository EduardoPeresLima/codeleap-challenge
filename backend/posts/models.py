from django.db import models

# Database Entities

# TODO: Maybe review later

class Post(models.Model):
    username = models.CharField(max_length=200) # Maybe define a max_length = 200 or smt?
    title = models.CharField(max_length=200)    # Same here
    content = models.TextField()  # Same here
    created_datetime = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ['-created_datetime']  # most recent first

    def __str__(self):
        return f"{self.username}: {self.title}"