import os
from setuptools import find_packages, setup

from syncasync import __version__


# We use the README as the long_description
readme_path = os.path.join(os.path.dirname(__file__), 'README.rst')


setup(
    name='syncasync',
    version=__version__,
    url='https://github.com/w1z2g3/syncasync',
    author='Django Software Foundation',
    author_email='foundation@djangoproject.com',
    description='Sync-to-async and async-to-sync function wrappers',
    long_description=open(readme_path).read(),
    license='BSD',
    zip_safe=False,
    py_modules=['syncasync'],
    include_package_data=True,
    extras_require={
        'tests': [
            'pytest~=3.3',
            'pytest-asyncio~=0.8',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
