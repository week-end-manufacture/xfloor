from setuptools import setup, find_packages

setup(
    name='xfloor',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'soupsieve'
    ],
    entry_points={
        'console_scripts': [
            'xfloor=main:main',
        ],
    },
    author='WEEK END MANUFACTURE',
    author_email='hyukzuny@gmail.com',
    description='An app that classifies file lists through crawling.',
    url='https://github.com/week-end-manufacture/xfloor',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)