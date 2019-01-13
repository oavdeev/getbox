#from distutils.core import setup
from setuptools import setup


setup(
    name='getbox',
    version='0.7.7',
    scripts=['bin/getbox'],
    author='Oleg Avdeev',
    author_email='feedback@instaguide.io',
    license='MIT license',
    url='https://github.com/oavdeev/getbox',
    description='Spot instance managing tool for AWS EC2',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='ec2 aws spot ssh',
    install_requires=['boto3>=1.5'],
)
