from setuptools import setup, find_packages

setup(
    name='dulu',
    version='0.1.4',
    packages=find_packages(), 
    install_requires=[
        'numpy==1.26.4',
        'opencv-python==4.10.0.84',
        'transformers==4.42.3',
        'torch==2.3.1',
        'timm==1.0.7',
        'einops==0.8.0'
    ],
    author='Krishna Sangeeth',
    author_email='kskrishnasangeeth@gmail.com',
    description='A Python library for OCR',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/whiletruelearn/florence_ocr',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
