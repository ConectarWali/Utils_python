from setuptools import setup, find_packages

setup(
    name='Utils_cws_web',
    version='1.0.0',
    description='Un paquete de middlewares para Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Conectar Wali SAS',
    author_email='dev@conectarwalisas.com.co',
    url='tecno.conectarwalisas.com.co',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
