import os
import setuptools
from numpy.distutils.core import setup


DISTNAME = 'matplotcheck'
DESCRIPTION = 'Functions to grade homework assignments in the Earth Analytics course'
MAINTAINER = 'Leah Wasser'
MAINTAINER_EMAIL = 'leah.wasser@colorado.edu'
VERSION = '0.0.1-git'


def configuration(parent_package='', top_path=None):
    if os.path.exists('MANIFEST'):
        os.remove('MANIFEST')

    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)

    config.add_subpackage('matplotcheck')

    return config


if __name__ == "__main__":
    setup(configuration=configuration,
          name=DISTNAME,
          maintainer=MAINTAINER,
          include_package_data=True,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          version=VERSION,
          install_requires=['tqdm', 'pandas', 'numpy', 'geopandas',
                            'matplotlib', 'rasterio', 'download', 'python-dateutil'],
          zip_safe=False,  # the package can run out of an .egg file
          classifiers=[
              'Intended Audience :: Developers',
              'License :: OSI Approved',
              'Programming Language :: Python',
              'Topic :: Software Development',
              'Operating System :: Microsoft :: Windows',
              'Operating System :: POSIX',
              'Operating System :: Unix',
              'Operating System :: MacOS'],)
