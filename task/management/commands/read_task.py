from django.core.management.base import BaseCommand, CommandError
from api.battleapi import call, CAREER_URL
from career.models import Career
from pyheroes import settings
from task.models import Task
class Command(BaseCommand):
    help = 'Reads the next task in queue and executes it'

    def handle(self, *args, **options):
        task = Task.objects.filter(started=False, ended=False)[:1]

        if task is Task.CAREER:
            url = CAREER_URL % (task.region, task.battletag_slug)

            career = Career()

            c, lm = call(url)

            career.fill_from_json(c)

        # self.stdout.write(career.data)
        # career = parser.career_profile(parser.EU_SERVER, 'Aveley', '2218')
        #
        # self.stdout.write(career.timePlayed.barbarian)
