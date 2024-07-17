from django.db import models

from tom_targets.base_models import BaseTarget


class UserDefinedTarget(BaseTarget):
    extra_bool = models.BooleanField(default=False)
    extra_number = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = "target"
        permissions = (
            ('view_target', 'View Target'),
            ('add_target', 'Add Target'),
            ('change_target', 'Change Target'),
            ('delete_target', 'Delete Target'),
        )
