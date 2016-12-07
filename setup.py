from setuptools import setup, find_packages
from setuptools.command.install import install


class BuildPackageProtos(install):
    def run(self):
        print "Running"
        from grpc.tools import command
        command.build_package_protos(self.distribution.package_dir[''])
        install.run(self)


setup(
    name='tensorflow_serving_python',
    version='0.1',
    description='Python client for tensorflow serving',
    author="Sebastian Schlecht",
    license="MIT",
    packages=['tensorflow_serving_python', 'tensorflow_serving_python.protos'],
    package_dir={'': 'src'},
    setup_requires=['cython', ],
    install_requires=[
        'tensorflow',
        'grpcio',
        'grpcio-tools'
    ],
    cmdclass={
        'install': BuildPackageProtos,
        'develop': BuildPackageProtos,
    }
)
