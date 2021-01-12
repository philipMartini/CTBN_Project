from setuptools import setup, find_packages


setup(name='PyCTBN',
      version='1.0',
      url='https://github.com/philipMartini/PyCTBN',
      license='MIT',
      author=['Alessandro Bregoli', 'Filippo Martini'],
      author_email=['a.bregoli1@campus.unimib.it', 'f.martini@campus.unimib.it'],
      description='A Continuous Time Bayesian Networks Library',
      packages=find_packages('.', exclude=['PyCTBN.tests']),
      #packages=['PyCTBN.classes'],
      install_requires=[
          'numpy', 'pandas', 'networkx', 'scipy', 'matplotlib', 'tqdm'],
      dependency_links=['https://github.com/numpy/numpy', 'https://github.com/pandas-dev/pandas',
                        'https://github.com/networkx/networkx', 'https://github.com/scipy/scipy',
                        'https://github.com/tqdm/tqdm'],
      long_description=open('README.md').read(),
      zip_safe=False,
      python_requires='>=3.6')
