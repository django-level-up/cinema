from .uuid import UUIDModel
from .time_stamp import TimeStampModel


class BaseModel(
    UUIDModel,
    TimeStampModel,
):
    """Base class"""

    class Meta:
        abstract = True
