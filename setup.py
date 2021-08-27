from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'readme.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='colloid_polymer_phase_diagram',
    version='0.3.1',
    description='A Python module to compute the phase behaviour of Colloid+Polymer mixture',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MathieuLeocmach/colloid-polymer-phase-diagram',
    author='Mathieu Leocmach',
    author_email='mathieu.leocmach@univ-lyon1.fr',  # Optional
    packages=["colloid_polymer_phase_diagram"],
    package_dir={'colloid_polymer_phase_diagram': 'colloid_polymer_phase_diagram'},
    install_requires=['numpy', 'scipy'],
    python_requires='>=2.5'
)
