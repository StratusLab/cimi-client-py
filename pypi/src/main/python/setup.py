import os
import os.path

from setuptools import setup


try:
    rootdir = os.path.join('python')
    for f in os.listdir(rootdir):
        src = os.path.join(rootdir, f)
        os.symlink(src, f)
except:
    # assume links have already been made
    pass

setup(
    name='stratuslab-cimi-client',
    version='${project.version}',

    author='StratusLab',
    author_email='support@stratuslab.eu',
    url='http://stratuslab.eu/',
    license='Apache Software License 2.0',
    description='${project.description}',
    long_description=open('README.txt').read(),
    keywords="IaaS cloud CIMI client",

    packages=[
        'cimi',
        'cimi.client',
        'cimi.client.api',
        'cimi.client.cli',
    ],

    entry_points={
        'console_scripts': [
            'cimi = cimi.client.cli.main:main',
        ],

        'cimi.client': [
            'cfg-set = cimi.client.cli.cfg:Set',
            'cfg-get = cimi.client.cli.cfg:Get',
            'cfg-delete = cimi.client.cli.cfg:Delete',
            'cfg-show = cimi.client.cli.cfg:Show',

            'collections = cimi.client.cli.resources:Collections',
            'show = cimi.client.cli.resources:Show',
            'list = cimi.client.cli.resources:List',
        ],
    },

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 2.6',
        'Topic :: System :: Distributed Computing',
    ],

    install_requires=[
        "requests >= 2.3.0",
        "cliff >= 1.5.2",
    ],
)
