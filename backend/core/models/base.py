from django.db import models
from django.conf import settings

class TimeStampedModel(models.Model):
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    deleted_dt = models.DateTimeField(null=True, blank=True)

    # created_by = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.SET_NULL,
    #     null=True, blank=True,
    #     related_name='%(class)s_created_by',
    # )

    # updated_by = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.SET_NULL,
    #     null=True, blank=True,
    #     related_name='%(class)s_updated_by',
    # )
    # deleted_by = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.SET_NULL,
    #     null=True, blank=True,
    #     related_name='%(class)s_deleted_by',
    # )

    class Meta:
        abstract = True