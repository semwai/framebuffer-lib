
from setuptools import setup

setup(
    name='framebuffer',
    version='0.1.2',
    description='library for interacting with /dev/fb0',
    long_description="""\
library for interacting with /dev/fb0
Display figures, drawings and the interface.""",
    keywords='framebuffer',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
    author='github.com/semwai',
    author_email='e14s@mail.ru',
    license='BSD',
    packages=['framebuffer'],
    install_requires=['numpy>=1.21.2', 'Pillow>=8.3.2', 'importlib-resources>=5.2.2'],
    package_data={'': ['framebuffer-lib.so']},
    include_package_data=True,
    zip_safe=False
)