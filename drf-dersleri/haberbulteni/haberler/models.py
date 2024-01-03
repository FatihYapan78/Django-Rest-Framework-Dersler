from django.db import models


class Gazeteci(models.Model):
    isim = models.CharField(max_length=50)
    soyisim = models.CharField(max_length=50)
    biyografi = models.TextField(blank=True,null=True)

    def __str__(self):
        return f'{self.isim} {self.soyisim}'


class Haber(models.Model):
    gazeteci = models.ForeignKey(Gazeteci, related_name="haberler", on_delete=models.CASCADE)
    baslik = models.CharField(max_length=50)
    metin = models.TextField()
    sehir = models.CharField(max_length=50)
    yayın_tarihi = models.DateField(auto_now_add=True)
    guncelleme_tarihi = models.DateField(auto_now=True)
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return self.baslik

