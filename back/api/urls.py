from django.urls import path

from api import views

urlpatterns = [
    path(
        'upload/',
        views.UploadFilesView.as_view(),
        name='upload'
    ),
    path(
        'files/',
        views.GetFilesListView.as_view(),
        name='files'
    ),
    path(
        'download/<int:file_id>/',
        views.DownloadFileView.as_view(),
        name='download'
    )
]
