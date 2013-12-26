import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder

from .decorators import ajax_required


class LoginRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class AjaxRequiredMixin(object):

    @method_decorator(ajax_required)
    def dispatch(self, *args, **kwargs):
        return super(AjaxMixin, self).dispatch(*args, **kwargs)


class AjaxMixin(AjaxRequiredMixin):
    """
    A mixin that raise 400 if request was not POST or was made not using ajax.
    Also render response as json.
    """
    response_class = HttpResponse

    def render_to_response(self, context=None, **response_kwargs):
        """
        Return a JSON response, transforming 'context' to make the payload.
        """
        response_kwargs['content_type'] = 'application/json'
        return self.response_class(self.convert_context_to_json(context or {}), **response_kwargs)

    def convert_context_to_json(self, context):
        """
        Convert the context dictionary into a JSON object
        """
        return json.dumps(context, cls=DjangoJSONEncoder)


class ActiveTabMixin(object):
    """
    Mixin to set active tab menu
    """
    active_tab = None

    def get_active_tab(self):
        if self.active_tab is None:
            raise ImproperlyConfigured(
                "ActiveTabMixin requires either a definition of "
                "'active_tab' or an implementation of 'get_active_tab()'")
        return self.active_tab

    def get_context_data(self, **kwargs):
        context = super(ActiveTabMixin, self).get_context_data(**kwargs)
        context['active_tab'] = self.get_active_tab()
        return context


class ReadOnlyAdminMixin(object):
    """
    Mixin for ModelAdmin to make it read only.
    """
    actions = None

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False if obj is not None else True

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return tuple(f.name for f in obj._meta.fields)
        return super(ReadOnlyAdminMixin, self).get_readonly_fields(request, obj)

    def __init__(self, *args, **kwargs):
        super(ReadOnlyAdminMixin, self).__init__(*args, **kwargs)
        self.list_display_links = (None, )
