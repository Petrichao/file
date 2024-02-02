from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import FileSerializer
from api.tasks import mod_file
from files.models import File


class UploadFilesView(APIView):
    """Эндпоинт для загрузки файлов на сервер"""
    def post(self, request, *args, **kwargs) -> Response:
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_instance = file_serializer.save()
            mod_file.apply_async(args=(file_instance.id,), countdown=0)
            return Response(
                file_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            file_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class GetFilesListView(APIView):
    """Эндпоинт для получения списка всех файлов"""
    def get(self, request, *args, **kwargs):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class DownloadFileView(APIView):
    """Эндпоинт для скачивания определенного файла"""
    def get(self, request, file_id):
        file_instance = get_object_or_404(File, id=file_id)
        file_path = file_instance.file.path
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = (f'attachment; filename="'
                                           f'{file_instance.file.name}"')
        return response
