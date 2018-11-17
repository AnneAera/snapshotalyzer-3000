from setuptools import setup
setup(
    name='snapshotalyzer-3000',
    version='0.1',
    author="Anne Wei",
    author_email='weiwei_214@yahoo.com',
    Description='SnapshotAlyzer 3000 is a tool to manage AWS EC2 snapshots',
    license="GPLv3",
    packages=['shotty'],
    url="https://github.com/sophie1127/snapshotalyzer-3000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',


)
