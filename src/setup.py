from setuptools import setup

setup(
    name='oxint',
    version='21.08',
    packages=['oxint', 'oxint.utils', 'oxint.utils.test', 'oxint.ingest', 'oxint.ingest.test', 'oxint.scraping',
              'oxint.scraping.test'],
    package_dir={'': 'src'},
    url='https://github.com/joaquinOnSoft/oxint',
    license='Apache License 2.0',
    author='Joaquín Garzón',
    author_email='',
    description='Tool to cross information from open sources and try to identify relations between different data.  '
)
