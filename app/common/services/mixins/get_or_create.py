from django.db import IntegrityError


class GetCreateServiceMixin:

    model = None

    def get_or_create(self, **kwargs):
        try:
            obj, created = self.model.objects.get_or_create(**kwargs)
            return obj, created
        except IntegrityError:
            return None, False
