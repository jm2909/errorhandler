# Copyright (c) 2008-2009 Simplistix Ltd, 2016 Chris Withers
# See license.txt for license details.

import os
from setuptools import setup

package_name = 'loghandler'
base_dir = os.path.dirname(__file__)

setup(
    name=package_name,
    version=open(os.path.join(base_dir,package_name,'version.txt')).read().strip(),
    author='Chris Withers, Joydeep Mukherjee',
    author_email='chris@simplistix.co.uk, jm29deep@gmail.com',
    license='MIT',
    description="A logging framework handler that tracks when messages above a certain level have been logged.",
    long_description=open(os.path.join(base_dir, 'README.rst')).read(),
    url='https://github.com/joydeep0929/errorhandler.git',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.8',
    ],
    packages=[package_name],
    zip_safe=False,
    include_package_data=True,
    extras_require=dict(
        test=['nose', 'nose-fixes', 'nose-cov', 'coveralls'],
        build=['sphinx', 'pkginfo', 'setuptools-git', 'wheel', 'twine']
    )
)
