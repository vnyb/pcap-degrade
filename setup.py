#!/usr/bin/env python3

"""
Setup pcap-degrade
"""

from os import path
from setuptools import setup

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='pcap-degrade',

    version='0.0.0',

    description='Degrade pcap captures',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/vnyb/pcap-degrade',

    author='Vianney Bajart',
    author_email='vianney.bajart@redmintnetwork.fr',

    license='Apache Software License',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: Telecommunications Industry',

        'Topic :: Software Development :: Testing :: Traffic Generation',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='pcap udp tcp rtp degrade mos packet loss latency',

    py_modules=[
        'pcap_degrade',
    ],

    install_requires=[
        'scapy-python3',
    ],

    extras_require={
    },

    package_data={
    },

    data_files=[
    ],

    entry_points={
        'console_scripts': [
            'pcap-degrade=pcap_degrade:main',
        ],
    },
)
