from distutils.core import setup

setup(name='netwaves',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Search for data tables.',
      url='https://github.com/tlevine/netwaves',
      py_modules=['netwaves'],
      install_requires = [
      ],
      scripts = [
          'netwaves',
      ],
      tests_require = ['nose'],
      version='0.0.1',
      license='AGPL',
      classifiers=[
          'Programming Language :: Python :: 3.4',
      ],
)
