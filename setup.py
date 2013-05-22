from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.easySslider.tile',
      version=version,
      description="Easyslider tile for collective.cover",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='collective cover easyslider',
      author='Espen Moe-Nilssen',
      author_email='espen@medialog.no',
      url='https://github.com/collective/collective.easySslider.tile',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.easySslider'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.easyslider',
          'collective.cover' 
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )


