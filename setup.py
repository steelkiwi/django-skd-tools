import os
import setuptools


SRC_ROOT = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(SRC_ROOT, 'requirements.txt')) as f:
    required = f.read().splitlines()


setuptools.setup(
    name="django-skd-tools",
    version="0.0.1",
    author="Steelkiwi",
    author_email="sites@steelkiwi.com",
    url="https://github.com/steelkiwi/django-skd-tools",
    license="MIT",
    description="Steelkiwi Django Tools",
    keywords="django tools helpers",
    packages=setuptools.find_packages(),
    install_requires=required,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    # tests_require=[],
    # test_suite='tests.runtests.runtests',
)
