from .serializers import BoardSerializer, BoardDetailSerializer
from .models import Board
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class BoardViewSet(APIView): # localhost가 안되면 127.0.0.1로 바꿔서
    def get(self, request, pk=None): # read
        if pk is None:
            boardlist = Board.objects.all()
            boardlist_serializer = BoardSerializer(boardlist, many=True)
            return Response(boardlist_serializer.data)
        else:
            boarddetail = Board.objects.get(pk=pk)
            boarddetaillist_serializer = BoardDetailSerializer(boarddetail) # many=True가 없어야 한다
            return Response(boarddetaillist_serializer.data)
    

    def post(self, request): # create
        boarddetaillist_serializer = BoardDetailSerializer(data=request.data)
            
        if boarddetaillist_serializer.is_valid():
            boarddetaillist_serializer.save()
            return Response(boarddetaillist_serializer.data)
        return Response(boarddetaillist_serializer.errors)


    def put(self, request, pk=None): # update-all
        boarddetail = Board.objects.get(pk=pk)
        boarddetaillist_serializer = BoardDetailSerializer(boarddetail, data=request.data)

        if boarddetaillist_serializer.is_valid():
            boarddetaillist_serializer.save()
            return Response(boarddetaillist_serializer.data)
        return Response(boarddetaillist_serializer.errors)


    def patch(self, request, pk=None): # update-part
        boarddetail = Board.objects.get(pk=pk)
        boarddetaillist_serializer = BoardDetailSerializer(boarddetail, data=request.data, partial=True)

        if boarddetaillist_serializer.is_valid():
            boarddetaillist_serializer.save()
            return Response(boarddetaillist_serializer.data)
        return Response(boarddetaillist_serializer.errors)


    def delete(self, request, pk=None): # delete
        boarddetail = Board.objects.get(pk=pk)
        boarddetail.delete()
        return Response({"message": "Article deleted successfully"}, status=status.HTTP_204_NO_CONTENT)