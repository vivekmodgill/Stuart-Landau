from setuptools import setup, find_packages

setup(
    name='stuart-landau',
    version='0.1',
    packages=find_packages(),
    author='Vivek Sharma',
    author_email='vivekmodgil@proton.me',
    description='A Python package for simulating the Stuart-Landau model.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/vivekmodgill/Stuart-Landau',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        'numpy',
        'numba',
        'scipy',
    ],
)
