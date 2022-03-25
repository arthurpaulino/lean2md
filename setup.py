from distutils.core import setup
from lean2md.__main__ import __version__

setup(
    name="lean2md",
    version=__version__,
    packages=['lean2md'],
    author='Arthur Leonardo de Alencar Paulino',
    author_email='arthurleonardo.ap@gmail.com',
    url='https://github.com/arthurpaulino/lean2md',
    description='Turns Lean files into markdown.',
    classifiers=['Intended Audience :: Developers',
                 'Intended Audience :: Science/Research',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'License :: OSI Approved :: MIT License']
)
