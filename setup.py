from setuptools import setup

setup_args = dict(
    name='nose-order-plugin',
    version='0.1',
    url='http://github.com/encukou/nose_order_plugin',
    maintainer='Petr Viktorin',
    maintainer_email='encukou@gmail.com',
    description='Nose test method ordering plugin',
    long_description=open('README').read(),
    install_requires=['nose'],
    license='GNU GPLv3+',
    py_modules=['nose_order_plugin'],
    zip_safe=False,
    entry_points={
        'nose.plugins.0.10': [
            'nose_order_plugin = nose_order_plugin:OrderTests'
            ]
        }
    )

if __name__ == '__main__':
    setup(**setup_args)
