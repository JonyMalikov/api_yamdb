from rest_framework import viewsets, mixins


class CRDViewSet(mixins.DestroyModelMixin,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 viewsets.GenericViewSet):
    pass
