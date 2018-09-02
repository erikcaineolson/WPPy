from setuptools import setup, find_packages

setup(name='wppy',
      version='1.0',
      description='Python script for rapidly generating WordPress sites on Linux NGINX servers from the command line',
      url='https://github.com/erikcaineolson/wppy',
      author='Erik C. Olson',
      author_email='erikcaineolson@gmail.com',
      license='MIT',
      packages=find_packages(),
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ], )
