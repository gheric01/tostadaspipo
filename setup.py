from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='PaqueteNuevo',
      version=version,
      description="Ejemplo de nuevo archivo",
      long_description="""\
Ejemplo de las tostadas de MAracaibo""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='package python egg conjuntos tostadas pipo',
      author='Gerardo Herice',
      author_email='gheric@cantv.com.ve',
      url='https://github.com/gheric01',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
