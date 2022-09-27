from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException
from rest_framework import exceptions


class ExportError(exceptions.APIException):
    status_code = 400
    default_detail = _("Export error")
    default_code = "export_error"


class ImportError(exceptions.APIException):
    status_code = 500
    default_detail = _("Import error")
    default_code = "import_error"


class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = "Service temporarily unavailable, please try again later."


class SerializerNotFound(Exception):
    pass
