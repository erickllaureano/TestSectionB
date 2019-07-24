from rest_framework.relations import RelatedField
from django.utils.translation import ugettext_lazy as _


class MultiSlugRelatedField(RelatedField):
    """
    Represents a relationship using a unique set of fields on the target.
    """

    default_error_messages = {
        'does_not_exist': _("Object with %s does not exist."),
        'invalid': _('Invalid value.'),
    }

    def __init__(self, slug_fields=None, **kwargs):
        assert slug_fields is not None, "slug_fields is required"
        self.slug_fields = slug_fields
        super(MultiSlugRelatedField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return dict(zip(
            self.slug_fields,
            (getattr(obj, slug_field) for slug_field in self.slug_fields),
        ))
