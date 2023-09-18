
import re
from rest_framework.serializers import ValidationError


class UrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        url_val = dict(value).get(self.field)
        if url_val:
            if bool(re.match(r'https://www.youtube.com/', url_val)) is False:
                raise ValidationError('Ссылка не корректная')


