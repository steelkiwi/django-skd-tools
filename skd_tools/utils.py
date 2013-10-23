import random
import os.path
import hashlib
from uuid import uuid4

from django.conf import settings
from django.core.files.storage import FileSystemStorage


def get_random_filename(instance, filename):
    """
    Generates random filename for uploading file using uuid4 hashes
    You need to define UPLOADS_ROOT in your django settings
    something like this
    UPLOADS_ROOT = rel(MEDIA_ROOT, 'uploads')
     """
    folder = settings.UPLOADS_ROOT
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(str(uuid4()), ext)
    return os.path.join(folder, filename)


def image_path(instance, filename):
    """Generates likely unique image path using md5 hashes"""
    filename, ext = os.path.splitext(filename.lower())
    instance_id_hash = hashlib.md5(str(instance.id)).hexdigest()
    filename_hash = ''.join(random.sample(hashlib.md5(filename.encode('utf-8')).hexdigest(), 8))
    return '{}/{}{}'.format(instance_id_hash, filename_hash, ext)


storage_factory = lambda root, url: FileSystemStorage(location=root, base_url=url)
