class UpdateServiceMixin:

    def update(self, instance, **kwargs):
        for attr, value in kwargs.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
