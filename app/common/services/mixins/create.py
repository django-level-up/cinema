class CreateServiceMixin:

    model = None

    def create(self, **kwargs):
        return self.model.objects.create(**kwargs)
