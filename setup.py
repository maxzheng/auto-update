import setuptools


setuptools.setup(
    name='autopip',
    version='0.0.2',

    author='Max Zheng',
    author_email='maxzheng.os@gmail.com',

    description='Top secret project',
    long_description=open('README.rst').read(),

    url='https://github.com/maxzheng/autopip',

    install_requires=open('requirements.txt').read(),

    license='MIT',

    packages=setuptools.find_packages(),
    include_package_data=True,

    python_requires='>=3.6',
    setup_requires=['setuptools-git'],

    entry_points={
       'console_scripts': [
           'app = autopip:main',
           'autopip = autopip:main',
       ],
    },

    # Standard classifiers at https://pypi.org/classifiers/
    classifiers=[
      'Development Status :: 1 - Planning',

      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',

      'License :: OSI Approved :: MIT License',

      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
    ],

    keywords='',
)