from setuptools import setup

setup(
    name='kural',
    version='0.0.1',
    description='A Library to make requests to GetThirukkural API',
    long_description='This is a wrapper to GetThirukkural API',
    keywords='kural api library tamil thirukkural',
    url='http://github.com/sanspace/kural',
    author='Santhosh Kumar Srinivasan',
    author_email='san@sanspace.in',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Tamil',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=['requests'],
)