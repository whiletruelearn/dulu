from setuptools import setup, find_packages

setup(
    name='dulu',
    version='0.1.2',
    packages=find_packages(), 
    install_requires=[
        'numpy',
        'opencv-python',
        'transformers',
        'torch',
        'timm',
        'einops'
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
