import sys

from setuptools import setup, find_packages

requirements = []
with open('requirements.txt') as f:
    for line in f: requirements.append(line.strip())
f.close()

version = None
if '--version' in sys.argv:
    index = sys.argv.index('--version')
    try:
        version = sys.argv[index + 1]
        version = version.split('/')[-1]
    except IndexError:
        print('version not specified')
        sys.exit(1)
    sys.argv.pop(index + 1)
    sys.argv.pop(index)

setup(
    name="uango_ros_web_socket",
    author='Miro',
    version=version,
    author_email='miroljubmihailovic98@gmail.com',
    install_requires=requirements,
    python_requires='>=3.12.0',
    packages=find_packages(exclude=['test', 'test.*']),
    include_package_data=True,
    package_data={
        'web_socket': ['text_parser/*.yaml', 'send_command/*.yaml']
    })
