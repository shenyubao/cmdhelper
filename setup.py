try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    

import os.path

setup(name='cmdhelper',
      version='0.2',
      description="A tool for cmd",
      long_description="""A tool for cmd""",
      author='Shenyubao',
      author_email='ssybb1988@gmail.com',
      url='http://www.shenyubao.com',
      packages=['cmdhelper'],
      package_dir={'cmdhelper':os.path.join('src','cmdhelper')},
      platforms = ["any"],
      scripts=[
          os.path.join('scripts','chdel'),
          os.path.join('scripts','chlist'),
          os.path.join('scripts','chrun'),
          os.path.join('scripts','chset'),
          os.path.join('scripts','chmark'),
          os.path.join('scripts','ch')
        ],
      keywords='cmd',
     )
