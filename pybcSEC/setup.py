from setuptools import setup


setup(
    name="pybcSEC",
    version="0.1.0",
    description="pybcSEC study tool for collecting Python package artifacts and scanning for bytecode evidence.",
    py_modules=[
        "analysis",
        "cli",
        "collectors",
        "scanner",
        "tool_analysis",
        "cpython_fuzz",
        "seed_extract",
        "source_repro",
        "crash_analysis",
        "rq1_analysis",
    ],
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "pybcSEC=cli:main",
        ],
    },
    python_requires=">=3.10",
)
