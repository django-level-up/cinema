class RetrieveServiceMixin:
    model = None

    def get(self, **kwargs):
        return self.model.objects.get(**kwargs)
