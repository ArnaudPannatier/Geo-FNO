"""Setup GEO-FNO package."""

from setuptools import find_packages, setup

__author__ = ""
__license__ = "MIT"
__maintainer__ = ""
__email__ = ""
__url__ = "https://github.com/ArnaudPannatier/Geo-FNO"
__version__ = "0.0"
__description__ = """Provide code for Geometry-Aware Fourier Neural Operator (Geo-FNO)"""

if __name__ == "__main__":
    with open("README.md") as f:
        long_description = f.read()
    setup(
        name="geofno",
        version=__version__,
        description=__description__,
        long_description=long_description,
        long_description_content_type="text/x-markdown",
        maintainer=__maintainer__,
        maintainer_email=__email__,
        url=__url__,
        license=__license__,
        classifiers=[
            "Intended Audience :: Science/Research",
            "Intended Audience :: Developers",
            "Topic :: Scientific/Engineering",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.10",
        ],
        packages=find_packages(include=["geofno","geofno*"]),
    )
