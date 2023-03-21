import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='visonicalarmlocal',
    version='0.0.1',
    author='Rémi Dartois',
    author_email='remi@dartoisr.fr',
    description='A simple library for the Visonic Alarm Local API written in Python 3.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dartoisr/visonicalarmlocal',
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
