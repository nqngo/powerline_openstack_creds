# vim:fileencoding=utf-8:noet

from setuptools import setup

setup(
    name             = 'powerline-openstack-creds',
    description      = 'A Powerline segment for showing current sourced Openstack credential',
    version          = '0.1.2',
    keywords         = 'powerline openstack_creds_helper',
    license          = 'MIT',
    author           = 'Nhat Ngo',
    author_email     = 'me@nqngo.com',
    url              = 'https://github.com/nqngo/powerline-openstack_creds',
    packages         = ['powerline_openstack_creds'],
    install_requires = ['powerline-status'],
    classifiers      = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Terminals'
    ]
)
