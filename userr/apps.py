# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class UserrConfig(AppConfig):
    name = 'userr'

    def ready(self):
        import userr.signals