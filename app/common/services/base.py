from common.services import mixins


class CRUDService(
    mixins.CreateServiceMixin,
    mixins.UpdateServiceMixin,
    mixins.ListServiceMixin,
    mixins.DeleteServiceMixin,
    mixins.FilterServiceMixin,
    mixins.RetrieveServiceMixin,
):
    """
    Base service with CRUD operations
    """

    def __init__(self):
        model = getattr(self.Meta, "model", None)
        if model is None:
            raise NotImplementedError(
                "You must define the 'model' attribute in the Meta class."
            )

        self.model = model
