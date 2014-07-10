django-skd-tools
================

- basic install: `pip install django-skd-tools`
- install with `TypedFileField` support: `pip install django-skd-tools[TypedFileField]`

Mixins
------

`skd_tools.mixins`

 - LoginRequiredMixin
 - AjaxRequiredMixin
 - AjaxMixin
 - ActiveTabMixin
 - ReadOnlyAdminMixin

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
    Max size taking MB(megabytes)
    Example:

    ```python
    file = TypedFileField(
        allowed_mimes=['application/pdf', 'image/png', 'image/jpeg',
                       'application/msword', 'application/zip'],
        allowed_exts=['doc', 'docx', 'jpeg', 'jpg', 'png', 'pdf'],
        max_size=10)
    ```
