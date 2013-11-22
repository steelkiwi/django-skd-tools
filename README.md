django-skd-tools
================

`pip install django-skd-tools`

Mixins
------

`skd_tools.mixins`

 - LoginRequiredMixin
 - AjaxRequiredMixin
 - AjaxMixin
 - ActiveTabMixin

Decorators
------

`skd_tools.decorators`

 - cache_method
 - cache_func
 - get_or_default
 - ajax_required

Utils
-----

`skd_tools.utils`

 - image_path
 - get_random_filename
 - storage_factory

Fields
-----

`skd_tools.fields`

 - TypedFileField


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
    Max size taking MB(megabytes)
