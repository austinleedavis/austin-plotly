from setuptools import setup

setup(
    packages=["austin_plotly"],
    description="Austin's personal Plotly utils - you're welcome to use, but this is very badly maintained and commented!.",
    install_requires=[
        "einops",
        "numpy",
        "torch",
        "plotly",
        "tqdm",
        "pandas",
    ],
)
