from django.shortcuts import render

from scores.models import Score
from scores.serializers import ScoreSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ScoreList(APIView):
    """
    List all scores, or create a new score.
    """
    def get(self, request, format=None):
        scores = Score.objects.all()
        serializer = ScoreSerializer(scores,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScoreDetail(APIView):
    """
    Retrieve, update or delete a score instance.
    """
    def get_object(self, pk):
        try:
            return Score.objects.get(pk=pk)
        except Score.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        score = self.get_object(pk)
        serializer = ScoreSerializer(score)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        score = self.get_object(pk)
        serializer = ScoreSerializer(score, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        score = self.get_object(pk)
        score.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
