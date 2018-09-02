from setuptools import setup

setup(name='wppy',
      version='1.0',
      description='Python script for rapidly generating WordPress sites from the command line',
      url='https://github.com/erikcaineolson/WPPy',
      author='Erik C. Olson',
      author_email='erikcaineolson@gmail.com',
      license='MIT',
      packages=['wppy', 'mysql-connector', 'python-dotenv'],
      zip_safe=False)
