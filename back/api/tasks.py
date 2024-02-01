from files.models import File
from celery import shared_task

import time


@shared_task
def mod_file(file_id):
    print(file_id)
    time.sleep(10)
    file_instance = File.objects.get(id=file_id)
    file_instance.processed = True
    file_instance.save()
