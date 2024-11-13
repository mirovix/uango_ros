from setuptools import setup, find_packages

requirements = []
with open('requirements.txt') as f:
    for line in f: requirements.append(line.strip())
f.close()

setup(
    name="uango_ros_web_socket",
    author='Miro',
    version="0.1.0",
    author_email='miroljubmihailovic98@gmail.com',
    install_requires=requirements,
    python_requires='>=3.12.0',
    packages=find_packages(exclude=['test', 'test.*']),
    include_package_data=True,
    package_data={
        'web_socket': ['text_parser/*.yaml', 'send_command/*.yaml']
    })
