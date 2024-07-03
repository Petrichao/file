from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='uploaded_files')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField()

    def __str__(self):
        return self.file.name


class Word(models.Model):
    word = models.CharField(max_length=50)
    tf = models.FloatField(default=0)
    df = models.FloatField(default=0)
    idf = models.FloatField(default=0)
    it_is_found_in = models.ManyToManyField(File)

    def __str__(self):
        return self.word
