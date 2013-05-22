from setuptools import setup, find_packages

with open('README.rst', 'r') as file:
    long_desc = file.read()

version = __import__('multipleselectfilter').get_version()

setup(
    name='django-multipleselectfilter',
    version=version,
    author='Mario Orlandi',
    author_email='morlandi@brainstorm.it',
    packages=find_packages(),
    scripts=[],
    url='https://github.com/morlandi/django-multiple-selection-filters',
    license='BSD',
    description='Add multiple selection filters to django admin listview.',
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
