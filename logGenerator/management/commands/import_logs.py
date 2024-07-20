import os
from django.core.management.base import BaseCommand
from logGenerator.models import NetworkLogs
from datetime import datetime

class Command(BaseCommand):
    help = 'Import network logs from a log file'

    def add_arguments(self, parser):
        parser.add_argument('logfile', type=str, help='The path to the log file')

    def handle(self, *args, **kwargs):
        logfile = kwargs['logfile']

        if not os.path.exists(logfile):
            self.stdout.write(self.style.ERROR(f'Log file "{logfile}" does not exist'))
            return

        with open(logfile, 'r') as file:
            for line in file:
                try:
                    parts = line.split(' - ')
                    datetime_str = parts[0]
                    datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S,%f')
                    bytes_sent_str = parts[2].split(': ')[1].split(',')[0]
                    bytes_received_str = parts[2].split(': ')[2]

                    log_entry = NetworkLogs(
                        datetime=datetime_obj,
                        bytes_sent=int(bytes_sent_str),
                        bytes_recieved=int(bytes_received_str)
                    )
                    log_entry.save()
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error processing line: {line}'))
                    self.stdout.write(self.style.ERROR(str(e)))

        self.stdout.write(self.style.SUCCESS('Log file imported successfully'))