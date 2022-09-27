from db_file_storage.form_widgets import DBAdminClearableFileInput
from django import forms
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.functions import Concat
from import_export import fields, resources, widgets
from import_export.admin import ImportExportModelAdmin


from nautobot.core.admin import NautobotModelAdmin

from .models import FileProxy, JobResult, Status


def order_content_types(field):
    """
    Order the list of available ContentTypes by application
    """
    queryset = field.queryset.order_by("app_label", "model")
    field.choices = [(ct.pk, f"{ct.app_label} > {ct.name}") for ct in queryset]


#
# File attachments
#


class FileProxyForm(forms.ModelForm):
    class Meta:
        model = FileProxy
        exclude = []
        widgets = {
            "file": DBAdminClearableFileInput,
        }


@admin.register(FileProxy)
class FileProxyAdmin(NautobotModelAdmin):
    form = FileProxyForm
    list_display = ["name", "uploaded_at"]
    list_filter = ["uploaded_at"]


#
# Job results (jobs, scripts, reports, Git repository sync, etc.)
#


@admin.register(JobResult)
class JobResultAdmin(NautobotModelAdmin):
    list_display = [
        "obj_type",
        "name",
        "created",
        "completed",
        "user",
        "status",
    ]
    fields = [
        "obj_type",
        "name",
        "created",
        "completed",
        "user",
        "status",
        "data",
        "job_id",
    ]
    list_filter = [
        "status",
    ]
    readonly_fields = fields

    def has_add_permission(self, request):
        return False


class ContentTypeManyToManyWidget(widgets.ManyToManyWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.model = ContentType
        self.field = "dotted_name"

    def get_queryset(self):
        queryset = self.model.objects.annotate(
            dotted_name=Concat("app_label", models.Value("."), "model", output_field=models.CharField())
        )
        return queryset

    def clean(self, value, row=None, *args, **kwargs):
        if not value:
            return self.model.objects.none()
        if isinstance(value, (float, int)):
            ids = [int(value)]
        else:
            ids = value.split(self.separator)
            ids = filter(None, [i.strip() for i in ids])

        # return self.model.objects.filter(**{
        queryset = self.get_queryset()
        return queryset.filter(**{"%s__in" % self.field: ids})

    def render(self, value, obj=None):
        content_types = obj.content_types.all()
        return ",".join(f"{ct.app_label}.{ct.model}" for ct in content_types)


class StatusResource(resources.ModelResource):
    content_types = fields.Field(attribute="content_types", widget=ContentTypeManyToManyWidget())

    class Meta:
        model = Status
        clean_model_instances = True
        export_order = ("name", "slug", "color", "content_types", "description")
        import_id_fields = (
            "name",
            "slug",
        )
        skip_unchanged = True
        fields = ("name", "slug", "color", "content_types", "description")


class StatusAdmin(ImportExportModelAdmin):
    resource_class = StatusResource


admin.site.register(Status, StatusAdmin)
