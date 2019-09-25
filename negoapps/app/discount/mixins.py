import datetime

import django_filters
from django.db import models
from rest_framework import viewsets, status, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ManagerMain(models.Manager):
    def get_queryset(self):
        return super(ManagerMain, self).get_queryset().filter(deleted_at__isnull=True)


class ManagerAllMain(models.Manager):
    def get_queryset(self):
        return super(ManagerAllMain, self).get_queryset()


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    objects = ManagerMain()
    objects_all = ManagerAllMain()

    class Meta:
        abstract = True


class DefaultViewSetMixin(object):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class ModelViewSet(viewsets.ModelViewSet):
    module_access = None

    # override method DELETE
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted_at = datetime.datetime.now()
        instance.save()
        response = {
            "result": "Ok"
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)
