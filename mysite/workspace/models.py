from django.db import models

class Reporter(models.Model):
    full_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.full_name

# Class for storing all the messages sent
class Message(models.Model):
    message_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date published")
