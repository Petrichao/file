from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from api.tasks import mod_file
from files.models import File
from api.serializers import FileSerializer


class UploadFilesView(APIView):
    def post(self, request, *args, **kwargs) -> Response:
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_instance = file_serializer.save()
            mod_file.apply_async(args=(file_instance.id,), countdown=0)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetFilesListView(APIView):
    def get(self, request, *args, **kwargs):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
