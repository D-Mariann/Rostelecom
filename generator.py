import random
from urllib.parse import urlparse
class StringForTest:
    def generate_num(self, n):
        psw = ''  # предварительно создаем переменную psw
        for x in range(n):
            psw = psw + random.choice(list('123456789'))
        return psw

    def generate_fraction(self, ):
        return random.random()
    def generate_string(self, n):
        return "x" * n

    def russian_chars(self,):
        return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def chinese_chars(self,):
        return '的一是不了人我在有他这为之大来以个中上们'

    def special_chars(self,):
        return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'

    def xss_application_html(self,):
        return '<img src="wrongSrc" onerror="alert(document.cookie)"/>'

    def application_svg(self,):
        return '<svg><script>alert(‘XSS’)</script></svg>'

    def xss_application_js(self,):
        return '<script>alert(document.cookie)</script>'

    def sql_application_js(self,):
        return "'); drop table keycloak.accounts; --test' OR 1=1 #"

    def payload(self,):
        return '<script>alert(document.cookie)</script>'

    def script(self,):
        return '<svg><script>alert(‘XSS’)</script></svg>'

def get_url_with_path(url):
    parsed = urlparse(url)
    base = parsed.netloc
    path = parsed.path
    with_path = base + path
    return with_path
