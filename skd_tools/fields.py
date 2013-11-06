import magic

from django import forms
from django.utils.translation import ugettext_lazy as _


class TypedFileField(forms.FileField):

    """
    Field for validation type of uploaded file
    Field take either "allowed_mimes" or "allowed_exts" lists
    with mimes or exts respectively

    Max size taking MB(megabytes)

    Example:
    file = TypedFileField(allowed_mimes=['application/pdf',
                                         'image/png', 'image/jpeg',
                                         'application/msword',
                                         'application/zip',
                                         'application/vnd.openxmlformats-officedocument.wordprocessingml.document'],
                          allowed_exts=['doc',
                                        'docx',
                                        'jpeg',
                                        'jpg',
                                        'png',
                                        'pdf'],
                          max_size=10)

    Or you can define FILE_UPLOAD_MAX_MEMORY_SIZE_CUSTOM and using is like,
    max_size=settings.FILE_UPLOAD_MAX_MEMORY_SIZE_CUSTOM
    """

    def __init__(self, *args, **kwargs):
        self.allowed_mimes = kwargs.pop('allowed_mimes', '')
        self.allowed_exts = kwargs.pop('allowed_exts', '')
        self.max_size = kwargs.pop('max_size', None)
        super(TypedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        value = super(TypedFileField, self).clean(*args, **kwargs)
        if value and (self.allowed_mimes or self.allowed_exts):
            mime = magic.from_buffer(value.read(1024), mime=True)
            ext = value.name.split('.')[-1].lower()
            if (mime not in self.allowed_mimes) or (ext not in self.allowed_exts):
                raise forms.ValidationError(_('This file extension does not support'))
        if value and self.max_size:
            if value.size/1024.0**2 > self.max_size:
                raise forms.ValidationError(_('This file is too big, max size {} MB'.format(self.max_size)))
        return value
