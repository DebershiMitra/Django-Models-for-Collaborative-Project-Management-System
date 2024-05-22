from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# role_choice = (
#     ("1","Admin"),
#     ("2", "Member")
# )
# class Team(models.Model):
#     name = models.CharField(max_length=20)
#     desc = models.CharField(max_length=50)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
#     created_on = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

class Project(models.Model):
    name = models.CharField(max_length=30, default="Untitled")
    desc = models.CharField(max_length=50, default=" ")
    start_date = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField(User, blank=True, null=True)

    def __str__(self):
        return self.name

# class TeamMembers(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     roles = models.CharField(max_length = 3, choices = role_choice, default = '2')

#     def __str__(self):
#         return self.roles


class Conversation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=255)
    message_type = models.CharField(max_length=20, default=" ")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message_text
    
class Resources(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    resource_type = models.CharField(max_length=20)
    resource_link = models.FileField(upload_to='pibot/resources')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_processed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return str(self.resource_link)
    
class PinnedItems(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


