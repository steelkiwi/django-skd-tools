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
    file = TypedFileField(
        allowed_mimes=('application/pdf', 'image/png', 'image/jpeg',
                       'application/msword', 'application/zip'),
        allowed_exts=('doc', 'docx', 'jpeg', 'jpg', 'png', 'pdf'),
        max_size=10)
    """
    default_error_messages = {
        'invalid_format': _("Wrong file format."),
        'invalid_size': _("This file is too big (max size is %(size)d MB).")
    }

    def __init__(self, *args, **kwargs):
        self.allowed_mimes = kwargs.pop('allowed_mimes', [])
        self.allowed_exts = kwargs.pop('allowed_exts', [])
        self.max_size = kwargs.pop('max_size', None)
        super(TypedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        value = super(TypedFileField, self).clean(*args, **kwargs)
        if value:
            mime = magic.from_buffer(value.read(1024), mime=True)
            value.seek(0)
            try:
                ext = value.name.split('.')[-1].lower()
            except IndexError:
                ext = ''
            if ((self.allowed_mimes and mime not in self.allowed_mimes) or
                    (self.allowed_exts and ext not in self.allowed_exts)):
                raise forms.ValidationError(self.error_messages['invalid_format'], code='invalid_format')
            if self.max_size and value.size / 1024.0 ** 2 > self.max_size:
                raise ValidationError(
                    self.error_messages['invalid_size'],
                    code='invalid_size',
                    params={'size': self.max_size},
                )
        return value
