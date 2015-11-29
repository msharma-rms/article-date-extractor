from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='articleDateExtractor',
    packages=['articleDateExtractor'],
    version='0.1',
    author='Ran Geva',
    author_email='ran@webhose.io',
    url='https://github.com/Webhose/article-date-extractor',
    license='MIT',
    description='Automatically extracts and normalizes an online article or blog post publication date',
    long_description=readme,
    install_requires=[
        "BeautifulSoup >= 3.2.1",
        "dateparser >= 0.3.1"
    ],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
        )
)