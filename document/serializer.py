from rest_framework import serializers
from .models import Document,Host

class HostSerializer(serializers.ModelSerializer):


    class Meta:
        model = Host
        fields = '__all__'



class DocSerializer(serializers.ModelSerializer):

    typed = serializers.ReadOnlyField(source='typed.typed')
    header = serializers.SerializerMethodField(required=False)
    bodys = serializers.SerializerMethodField(required=False)
    querys = serializers.SerializerMethodField(required=False)
    param =  serializers.SerializerMethodField(required=False)
    urls = serializers.SerializerMethodField(required=False)


    class Meta:

        model = Document
        # fields = '__all__'
        exclude = ['headers','body','query','params','url']

    def get_header(self,obj):
        headers = obj.headers
        try:
            header = eval(headers)
        except:
            return []
        return header

    def get_bodys(self,obj):
        body = obj.body
        try:
            body = eval(body)
        except:
            return []
        return body

    def get_querys(self,obj):
        query = obj.query
        try:
            query = eval(query)
        except:
            return []
        return query

    def get_param(self,obj):
        param = obj.params
        print(param)
        try:
            param = eval(param)
        except Exception as e:
            print(e)
            return []
        return param

    def get_urls(self,obj):
        return obj.typed.host[:-1] + obj.url
