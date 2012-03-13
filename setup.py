from distutils.core import setup

setup(
    name='python-redmine',
    version='0.1',
    long_description=open('README.rst').read(),
    description='Python Redmine Web Services Library',
    author=' Ian Epperson',
    url='http://code.google.com/p/pyredminews/',
    py_modules=['redmine'],
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Environment :: Console',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Utilities'],    
)