from setuptools import setup, find_packages

setup(
    name="sistema-distribuido-pedidos",
    version="1.0.0",
    author="John Serrano",
    author_email="jserranoc2@ejemplo.com",
    description="Sistema distribuido para la gestión de pedidos con Flask, MySQL, Kafka, y Docker.",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "Flask",
        "kafka-python",
        "mysql-connector-python"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
