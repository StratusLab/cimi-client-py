from distutils.core import setup

import os
import os.path

try:
    rootdir = os.path.join('python')
    for file in os.listdir(rootdir):
        src = os.path.join(rootdir, file)
        os.symlink(src, file)
except:
    # assume links have already been made
    pass

setup(
    name='stratuslab-cimi-client',
    version='${project.version}',
    author='StratusLab',
    author_email='contact@stratuslab.eu',
    url='http://stratuslab.eu/',
    license='Apache Software License 2.0',
    description='${project.description}',
    long_description=open('README.txt').read(),

#    scripts=[
#        'bin/cimi',
#        ],

     packages=[
        'cimi',
        'cimi.client',
        ],

#    data_files=[
#        ('java', ['java/metadata-${metadata.version}-jar-with-dependencies.jar']),
#        ('share/vm', ['share/vm/schema.one']),
#        ('share/template', ['share/template/manifest.xml.tpl']),
#        ('conf', ['conf/stratuslab-user.cfg.ref']),
#        ('Scripts', ['windows/cimi.bat']),
#        ],

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
        "requests >= 1.2.3",
    ],
)
