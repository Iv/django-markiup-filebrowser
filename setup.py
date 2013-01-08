from setuptools import setup
import subprocess
import os.path


long_description = (open('README.rst').read() +
                    open('CHANGES.rst').read() +
                    open('TODO.rst').read())


def _static_files(prefix):
    return [prefix+'/'+pattern for pattern in [
        'markitup_filebrowser/*.*',
        'markitup_filebrowser/templates/*.*'
    ]]


setup(
    name='django-markitup-filebrowser',
    version='0.0.1',
    description='Filebrowser interface to MarkItUp! universal editor',
    long_description=long_description,
    author='Ivan Kravchenko',
    author_email='iv.kravchenko@gmail.com',
    url='http://bitbucket.org/carljm/django-markitup/',
    packages=['markitup_filebrowser', 'markitup_filebrowser.templatetags'],
    classifiers=[
        'Development Status :: 1 - Development/Unstable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    test_suite='runtests.runtests',
    tests_require='Django>=1.3',
    package_data={'markitup_filebrowser': ['templates/markitup_filebrowser/*.html'] +
                              _static_files('static')}
)
