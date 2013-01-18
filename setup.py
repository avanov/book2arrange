import os
import sys

from setuptools import find_packages
from setuptools import setup



PY3K = sys.version_info >= (3,0)
readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name='book2arrange',
    version='1.0.0',
    packages=find_packages(exclude=['tests']),
    install_requires=[],
    setup_requires=[],
    tests_require=[],
    package_data={
        # If any package contains listed files, include them
        '':['*.txt', '*.rst']
    },
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'book2arrange = book2arrange:main',
            ]
    },
    # PyPI metadata
    # Read more on http://docs.python.org/distutils/setupscript.html#meta-data
    author="Maxim Avanov",
    author_email="maxim.avanov@gmail.com",
    maintainer="Maxim Avanov",
    maintainer_email="maxim.avanov@gmail.com",
    description="Arrange audio files from http://www.50languages.com/ in one "
                "convenient collection for better language acquisition.",
    long_description=readme,
    license="MIT",
    url="https://github.com/2nd/book2arrange",
    download_url="https://github.com/2nd/book2arrange",
    keywords="cli utils foreign language education",
    # See the full list on http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Education',
        ]
)
