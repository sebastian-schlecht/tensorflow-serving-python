import setuptools
from setuptools.command.install import install

class BuildPackageProtos(install):
  def run(self):
    print "Running"
    from grpc.tools import command
    command.build_package_protos(self.distribution.package_dir[''])
    install.run(self)

setuptools.setup(
  name='tensorflow_serving_python',
  verions='0.1',
  description='Python client for tensorflow serving',
  author = "Sebastian Schlecht",
  license = "MIT",
  package_dir = {'': 'tensorflow_serving_python'},
  package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['protos/*.proto'],
    },
  setup_requires=[
          'tensorflow',
          'grpcio',
          'cython',
          'grpcio-tools'
      ],
  cmdclass={
    #'install': BuildPackageProtos,
  }
)
