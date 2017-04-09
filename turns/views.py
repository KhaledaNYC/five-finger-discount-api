from django.shortcuts import render

from turns.models import Turn
from turns.serializers import TurnSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TurnList(APIView):
    """
    List all turns, or create a new turn.
    """
    def get(self, request, format=None):
        turns = Turn.objects.all()
        serializer = TurnSerializer(turns,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TurnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TurnDetail(APIView):
    """
    Retrieve, update or delete a turn instance.
    """
    def get_object(self, pk):
        try:
            return Turn.objects.get(pk=pk)
        except Turn.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        turn = self.get_object(pk)
        serializer = TurnSerializer(turn)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        turn = self.get_object(pk)
        serializer = TurnSerializer(turn, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        turn = self.get_object(pk)
        turn.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
