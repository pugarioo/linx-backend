from django.db import models
import string
import random
import uuid

# Create your models here.
def generate_code():
    length = 6

    chars = string.ascii_letters + string.digits

    while True:
        code = ''.join(random.choice(chars) for _ in range(length))

        if not Link.objects.filter(short_code=code).exists():
            return code
        
class Link(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    orig_url = models.URLField(
        max_length=2000,
        unique=False,
        verbose_name='Original URL'
    )

    short_code = models.CharField(
        max_length=8,
        unique=True,
        default=generate_code,
        verbose_name='Short Code'   
    )

    clicks = models.IntegerField(
        default=0,
        verbose_name='Click Count'
    )

    last_clicked = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Sort links by creation date, newest first
        ordering = ['-created_at'] 
        verbose_name = "Short Link"
        verbose_name_plural = "Short Links"

    def __str__(self):
        return f"/{self.short_code} -> {self.original_url[:50]}..."

    def save(self, *args, **kwargs):
        """Override save to ensure short_code is set if it's missing."""
        if not self.short_code:
            self.short_code = generate_code()
        super().save(*args, **kwargs)
    