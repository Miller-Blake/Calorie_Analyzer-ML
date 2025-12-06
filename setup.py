from setuptools import setup, find_packages

setup(
    name="calorie_analyzer",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas",
        "openpyxl",
        "scikit-learn",
        "matplotlib",
        "typer",
    ],
    entry_points={
        "console_scripts": [
            "health = calorie_analyzer.main:app",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python CLI tool for calorie and weight analysis.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/YourUsername/is4010-final-calorie-analyzer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)