class ListServiceMixin:
    model = None

    def all(self):
        return self.model.objects.all()
