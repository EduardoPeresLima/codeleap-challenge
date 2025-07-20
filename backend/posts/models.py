from django.db import models

# Database Entities

class Post(models.Model):
    username = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ['-created_datetime']  # most recent first

    def __str__(self):
        return f"{self.username}: {self.title}"

class Comment(models.Model):
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, # When deleting a post, all their comments will delete as well
        related_name='comments'
    )
    parent_comment = models.ForeignKey(
        'self', 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE, # When deleting a comment, all their inside comments will delete as well
        related_name='replies'
    )
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=200)

    def __str__(self):
        return f"Comment {self.id} on Post {self.post.id}"