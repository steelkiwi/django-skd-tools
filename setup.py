import setuptools


setuptools.setup(
    name="django-skd-tools",
    version="0.2.2",
    author="Steelkiwi",
    author_email="vilisov@steelkiwi.com",  # temp
    url="https://github.com/steelkiwi/django-skd-tools",
    license="MIT",
    description="Steelkiwi Django Tools",
    keywords="django tools helpers",
    packages=setuptools.find_packages(),
    extras_require={'TypedFileField': ['python-magic==0.4.6']},
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'])
