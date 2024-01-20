class DeleteServiceMixin:

    def delete(self, instance):
        instance.delete()
