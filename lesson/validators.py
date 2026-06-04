import re
from rest_framework.serializers import ValidationError
class LinkYT:
    def __init__(self, field = "video"):
        self.field=field

    def __call__(self, value):
        reg = re.compile(r'^(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)\w+')
        if not reg.match(value):
            raise ValidationError("Ссылка не принадлежит YouTube")


