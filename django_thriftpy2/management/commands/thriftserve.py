from django.core.management.base import BaseCommand
from django.conf import settings

from ...server import rpc


class Command(BaseCommand):
    """Run a development thrift server"""

    def handle(self, *args, **kwargs):
        rpc.make_server()
