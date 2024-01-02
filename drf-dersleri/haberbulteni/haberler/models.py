from django.db import models

class Haber(models.Model):
    gazeteci = models.CharField(max_length=50)
    baslik = models.CharField(max_length=50)
    metin = models.TextField()
    sehir = models.CharField(max_length=50)
    yayın_tarihi = models.DateField(auto_now_add=True)
    guncelleme_tarihi = models.DateField(auto_now=True)
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return self.baslik

