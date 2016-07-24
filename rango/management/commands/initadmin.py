from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db.utils import IntegrityError


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            # Better change the password once it has been created
            User.objects.create_superuser(username='admin',
                                          password='admin',
                                          email='')
        except IntegrityError:
            # TODO: Hack to create superuser;
            # need a check to validate if superuser exists or not
            pass
