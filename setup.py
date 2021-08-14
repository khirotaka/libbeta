from setuptools import setup, find_namespace_packages
from setuptools_rust import Binding, RustExtension


setup(
    name="libbeta",
    version="0.1.0",
    packages=find_namespace_packages(include=["libbeta.*"]),
    zip_safe=False,
    rust_extensions=[
        RustExtension(
            "libbeta.rust",
            path="Cargo.toml",
            binding=Binding.PyO3,
            debug=False,
        ),
        RustExtension(
            "libbeta.utils",
            path="Cargo.toml",
            binding=Binding.PyO3,
            debug=False,
        )
    ],
)
