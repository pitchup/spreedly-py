from distutils.core import setup

setup(
    name='spreedly-py',
    version='0.1.0',
    author='M. Codona',
    author_email='mike@pitchup.com',
    packages=['spreedly', 'spreedly.payment_methods', 'spreedly.transactions', 'spreedly.common'],
    description='Python port of spreedly-gem.',
    long_description=open('README.md').read(),
    install_requires=[
        "requests==1.2.3",
        "lxml==4.9.1",
    ],
)


