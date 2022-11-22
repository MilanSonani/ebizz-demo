from django.db import models
from colorfield.fields import ColorField

class Tag(models.Model):
    name = models.CharField(max_length=50, blank=True)
    bgcolor = ColorField(format='hexa', default="#3a87ad")
    color = ColorField(format='hexa', default="#ffffff")

    def __str__(self):
        return str(self.name)


class Todo(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Tag, related_name="todo_tags", on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)
