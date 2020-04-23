from setuptools import setup, find_packages

setup(
    name='mic',
    version="1.0",
    description="Medical Image Changer",
    author="Myung Ki Cho",
    author_email="chobe0719@gmail.com",
    url="https://github.com/chobe111/medicalImageChanger.git",
    install_requires=[
        "tensorflow>=1.14.0",
        "SimpleITK>=1.2.4",
        "Pillow>=7.1.1",
        "mritopng==2.2",
    ],
    packages=find_packages(exclude=['test_jupyter/', 'venv/']),
    keywords=["medical image", "image change"],
    python_requires='>=3',
    zip_safe=False
)
