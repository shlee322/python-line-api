from distutils.core import setup
setup(
    name='line-api',
    version = '0.0.1-dev',
    py_modules = [
        'line',
        'line.messaging',
        'line.messaging.events'
    ],
    author = 'Sanghyeok Lee',
    author_email = 'shlee322@elab.kr',
    url='https://github.com/shlee322/python-line-api',
    description = 'SDK of the LINE Messaging API for Python',
)
