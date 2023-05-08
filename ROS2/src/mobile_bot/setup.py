from setuptools import setup

package_name = 'mobile_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jakub',
    maintainer_email='jakub@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'velocity=mobile_bot.motor_pwm:main',
        'person_follower=mobile_bot.person_follow:main',
        'ultrasonic_sensor=mobile_bot.sonar_sensor:main',
        ],
    },
)
