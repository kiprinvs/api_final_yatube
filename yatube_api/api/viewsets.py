from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet


class CreateAndListOnlyModelViewSet(
    CreateModelMixin, ListModelMixin, GenericViewSet
):
    pass
