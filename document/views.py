from django.shortcuts import render
from .models import Document,Host
from rest_framework.views import APIView
from rest_framework import generics
from .serializer import DocSerializer
from rest_framework.response import Response


class Api(generics.ListAPIView):

    serializer_class = DocSerializer

    def get_queryset(self):
        typed = self.kwargs.get('apiType')
        querysets = Document.objects.select_related().filter(typed__typed=typed)
        return querysets

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        types = Host.objects.all().values('typed')
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        typed = self.kwargs.get('apiType')

        return render(self.request,'index.html',{'api_list':data,"type":typed,'types':types})



