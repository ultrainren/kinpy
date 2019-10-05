from setuptools import setup

__version__ = '0.0.1'

setup(
    name='kinpy',
    version=__version__,
    author='neka-nat',
    author_email='nekanat.stock@gmail.com',
    description='Robotics kinematic calculation toolkit',
    license='MIT',
    keywords='robot kinematics',
    url='http://github.com/neka-nat/kinpy',
    packages=['kinpy'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['numpy', 'scipy', 'absl-py',
                      'urdf-parser-py', 'transformations',
                      'vtk'],
)