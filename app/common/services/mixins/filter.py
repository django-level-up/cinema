class FilterServiceMixin:
    model = None

    def filter(self, **kwargs):
        return self.model.objects.filter(**kwargs)
