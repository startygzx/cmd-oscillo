# -*- coding: utf-8 -*-
try:
    import setuptools
except ImportError:
    import distutils.core as setuptools

__VERSION__ = '0.1.0'

requirements = [
    'psutil==5.2.2',
    'matplotlib==2.1.0',
    'numpy==1.13.1',
    'PyYAML==3.13',
]

test_requirements = ['mock']

packages = setuptools.find_packages(
    exclude=['tests', 'tests.*'])
setuptools.setup(
    name='oscillo',
    description="Record the system load at the execution of the command line and display it graphically",
    version=__VERSION__,
    author='Rao Mengnan',
    author_email="raomengnan@gmail.com",
    maintainer='Rao Mengnan',
    maintainer_email='raomengnan@gmail.com',
    url='https://blog.atomicer.cn',
    packages=packages,
    package_data={'': ['LICENSE', 'requirements.txt']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Customer Service',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    entry_points={
        'console_scripts': [
            'oscillo = oscillo:main',
        ]
    },
    platforms=['Independent'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    tests_require=test_requirements,
    test_suite='tests'
)
