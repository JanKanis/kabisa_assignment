from django.core.serializers.json import DjangoJSONEncoder
from django.db import models

class Quote(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    author = models.CharField(max_length=255)
    quote = models.TextField()
    retrieval_date = models.DateTimeField(auto_now_add=True, blank=True)
    likes = models.IntegerField(default=0, blank=True)

    def as_dict(self):
        return dict(
            id=self.id,
            author=self.author,
            quote=self.quote,
            retrieval_date=self.retrieval_date,
            likes=self.likes
        )

    def get_absolute_url(self):
        return f'/quote/{self.id}/'
    def text(self):
        return f"{self.quote}"
    def __str__(self):
        return f"{self.id}: {self.quote} ({self.likes} likes)"


class QuoteEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Quote):
            g