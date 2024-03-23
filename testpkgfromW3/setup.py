from setuptools import find_packages, setup

package_name = 'testpkgfromW3'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='acrtmac1',
    maintainer_email='acrtmac@gmail.com',
    description='a good description ',
    license='RMIT IP - Not for distribution',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            f"testpkgfromW3 = {package_name}.testpkgfromW3:main",
        ],
    },
)
