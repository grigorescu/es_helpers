from setuptools import setup
setup(
    name = "es_helpers",
    version = "0.1-r3",
    packages = ["es_helpers"],
    install_requires = ["requests==0.13.6"],
    entry_points = {
        'console_scripts': [
            'es_cleanup = es_helpers.es_cleanup:delete',
            'es_optimize = es_helpers.es_optimize:optimize',
            ]
    }
)
