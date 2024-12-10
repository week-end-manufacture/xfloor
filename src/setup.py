from setuptools import setup, find_packages

setup(
    name='xfloor',
    version='0.0.3',
    packages=find_packages(include=['libj', 'libj.*']),
    py_modules=['main'],
    install_requires=[
        'beautifulsoup4',
        'soupsieve',
        'setuptools',
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