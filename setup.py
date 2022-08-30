from setuptools import setup, find_packages
from os.path import join, dirname
import yandex_360

setup(
    name='yandex_360',
    version=yandex_360.__version__,
    packages=find_packages(),
    description='Yandex 360 Lib',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    author=yandex_360.__author__,
    author_email='ya360@uh.net.ru',
    maintainer=yandex_360.__author__,
    maintainer_email='ya360@uh.net.ru',
    download_url='https://github.com/imercury13/yandex_360',
    #url='https://ya360.uh.net.ru',
    license='MIT',
    project_urls={
        "Documentation": "https://yandex-360.readthedocs.io/ru/1.3.0/",
        "Bug Tracker": "https://github.com/imercury13/yandex_360/issues"
    },
    classifiers=[
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python'
    ],
    install_requires=[
        'jreq',
    ],
    include_package_data=True,
)
