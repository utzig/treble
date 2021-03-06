# Copyright 2019 Carles Cufí.
# Copyright 2019 Nordic Semiconductor ASA.
#
# SPDX-License-Identifier: Apache-2.0

import setuptools

with open('README.rst', 'r') as f:
    long_description = f.read()

with open('treble/version.py', 'r') as f:
    exec(f.read())

setuptools.setup(
    name='treble',
    version=__version__,
    author='Carles Cufí',
    author_email='carles.cufi@nordicsemi.no',
    description='Python BLE Host',
    long_description=long_description,
    # http://docutils.sourceforge.net/FAQ.html#what-s-the-official-mime-type-for-restructuredtext-data
    long_description_content_type="text/x-rst",
    url='https://github.com/carlescufi/treble',
    packages=setuptools.find_packages(where='.'),
    #package_dir={'': 'treble'},
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
    ],
    install_requires=[
        'typing-extensions;python_version<"3.8"',
        'pyserial',
        'prompt_toolkit',
    ],

    entry_points={'console_scripts': ('treble = treble.cli:main',)},
    python_requires='>=3.7',
)
