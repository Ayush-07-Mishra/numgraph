from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="numgraph",
    version="0.1.0",
    author="Ayush Mishra",
    description="A Python library that converts mathematical equations into graph structures for visualization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ayushmishra/numgraph",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "sympy>=1.12",
        "networkx>=3.1",
        "matplotlib>=3.7.0",
        "pyvis>=0.3.2",
        "numpy>=1.24.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
        ],
    },
)
