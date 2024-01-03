from rest_framework import serializers
from haberler.models import *
from datetime import datetime
from django.utils.timesince import timesince


class HaberSerializer(serializers.ModelSerializer):
    yayın_tarihi_üzerinden_gecen_süre = serializers.SerializerMethodField()
    class Meta:
        model = Haber
        fields = "__all__"
        # exclude = ["gazeteci"] Hariç tut
        read_only_fields = ["id","yayın_tarihi","guncelleme_tarihi"]

    def get_yayın_tarihi_üzerinden_gecen_süre(self,object):
        now = datetime.now()
        yayin_tarihi = object.yayın_tarihi
        gecen_sure = timesince(yayin_tarihi,now)
        return gecen_sure

    def validate(self,data):
        if data["baslik"] == data["metin"]:
            raise serializers.ValidationError(
                "Başlık alanı ile metin alanı içeriği aynı olamaz. Lütfen değiştirin."
            )
        return data
    
    def validate_baslik(self,baslik):
        if len(baslik) < 15:
            raise serializers.ValidationError(
                "Başlık alanı 15 karakterden küçük olamaz."
            )
        return baslik
    
class GazeteciSerializer(serializers.ModelSerializer):
    # haberler = HaberSerializer(many=True,read_only=True)
    haberler = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="haber"
    )
    class Meta:
        model = Gazeteci
        fields = "__all__"