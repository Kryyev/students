# gmail.com, yahoo.com, icloud.com
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

@deconstructible
class ValidEmailDomain:
    def __init__(self, *domains):
        self.domains = list(domains)

    def __call__(self, *args, **kwargs):
        for domain in self.domains:
            if args[0].endswith(domain):
                break
        else:
            raise ValidationError(f'Incorrect email <{args[0].split("@")[1]}> is invalid')