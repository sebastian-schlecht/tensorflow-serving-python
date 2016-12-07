from setuptools import setup
from setuptools.command.install import install

import os


class BuildPackageProtos(install):
    def run(self):
        install.run(self)
        os.system('pip install cython')
        os.system('pip install grpcio')
        os.system('pip install grpcio-tools')
        from grpc.tools import command
        command.build_package_protos(self.distribution.package_dir[''])


setup(
    name='tensorflow_serving_python',
    version='0.1',
    description='Python client for tensorflow serving',
    author="Sebastian Schlecht",
    license="MIT",
    packages=['tensorflow_serving_python', 'tensorflow_serving_python.protos'],
    package_dir={'': 'src'},
    setup_requires=['cython'],
    install_requires=[
        'grpcio', 'grpcio-tools',
        'tensorflow',
    ],
    cmdclass={
        'install': BuildPackageProtos,
        'develop': BuildPackageProtos,
    }
)
