from setuptools import setup, find_packages

with open('README.rst', 'r') as file:
    long_desc = file.read()

version = __import__('extraadminfilters').get_version()

setup(
    name='django-adminfilters',
    version=version,
    author='Kevin Van Wilder',
    author_email='kevin@van-wilder.be',
    packages=find_packages(),
    scripts=[],
    url='https://github.com/kevwilde/django-extra-admin-filters',
    license='BSD',
    description='Additional change list filters for django admin.',
    long_description=long_desc,
    include_package_data=True,
    zip_safe=False,
    install_requires=(
    ),
    classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Utilities'
    ],
)
