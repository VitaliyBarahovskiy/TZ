# from django.shortcuts import render
from rest_framework import generics
from proba.serializers import ProbDetailSerializer, ProbaListSerializer
from proba.models import Prob
from django_filters.rest_framework import DjangoFilterBackend
from .service import ProbFilter


class ProbCreateView(generics.CreateAPIView):
    serializer_class = ProbDetailSerializer


class ProbaListView(generics.ListAPIView):
    serializer_class = ProbaListSerializer
    queryset = Prob.objects.all
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProbFilter

class ProbDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProbDetailSerializer
    queryset = Prob.objects.all()
