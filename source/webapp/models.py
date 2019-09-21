from django.db import models

STATUS_CHOICES = (
    ('active', 'Active'),
    ('blocked', 'Blocked'),
)
class Guestbook(models.Model):
    author = models.CharField(max_length=50, null=False, blank=False, verbose_name='author')
    email = models.EmailField(max_length=70, null=False, blank=False, verbose_name='email')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField(max_length=20, default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)

    def __str__(self):
        return self.author