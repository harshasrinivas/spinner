from setuptools import setup

setup(name='spinning',
      description='spinning animation',
      version='0.1.0',
      author='Harsha Srinivas',
      author_email='95harsha95@gmail.com',
      packages=['spinning'],
      entry_points={
          'console_scripts': ['spinning=spinning:main'],
      },
      install_requires=[
          'future',
          'blessings',
      ],
      url='https://github.com/harshasrinivas/spinning/',
      keywords=['python', 'animation', 'beautify', 'cli', 'spinner'],
      classifiers=[
          'Operating System :: POSIX',
          'Environment :: Console',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Topic :: Utilities',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],)
