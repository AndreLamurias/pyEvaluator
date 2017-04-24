try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pyEvaluator',
    version='0.1',
    packages=['pyEvaluator'],
    author='Luis Campos',
    author_email='luis.filipe.lcampos@gmail.com',
    url='https://github.com/LLCampos/pyEvaluator',
    license='',
    install_requires=[
        'requests',
        'sklearn',
        'numpy',
        'scipy',
    ],
)
