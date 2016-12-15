try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='evaluator',
    version='0.1',
    packages=['Evaluator'],
    author='Lu\xc3\xads Campos',
    author_email='luis.filipe.lcampos@gmail.com',
    url='https://github.com/LLCampos/evaluator',
    license='',
    install_requires=[
        'requests'
    ],
)
