
from django.core.validators import RegexValidator, _lazy_re_compile

slug_re = _lazy_re_compile(r'^[-a-zA-Z0-9_]+\Z')
user_slug = RegexValidator(
    slug_re,
    # Translators: "letters" means latin letters: a-z and A-Z.
    ('Введите корректное имя пользователя. Могут использоваться только латинские символы и цифры.'),
    'invalid'
)