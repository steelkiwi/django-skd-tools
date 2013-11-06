import magic

from django import forms
from django.utils.translation import ugettext_lazy as _


class TypedFileField(forms.FileField):

    """
    Field for validation type of uploaded file
    Field take either "allowed_mimes" or "allowed_exts" lists
    with mimes or exts respectively

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
                                        'pdf'])

    """

    def __init__(self, *args, **kwargs):
        self.allowed_mimes = kwargs.pop('allowed_mimes', '')
        self.allowed_exts = kwargs.pop('allowed_exts', '')
        super(TypedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        value = super(TypedFileField, self).clean(*args, **kwargs)
        if value and (self.allowed_mimes or self.allowed_exts):
            mime = magic.from_buffer(value.read(1024), mime=True)
            ext = value.name.split('.')[-1].lower()
            if (mime not in self.allowed_mimes) or (ext not in self.allowed_exts):
                raise forms.ValidationError(_('This file extension does not support'))
        return value
