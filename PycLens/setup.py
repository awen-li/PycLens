from setuptools import setup


setup(
    name="PycLens",
    version="0.1.0",
    description="PycLens empirical study tool for Python bytecode artifacts.",
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
            "pyclens=cli:main",
        ],
    },
    python_requires=">=3.10",
)
