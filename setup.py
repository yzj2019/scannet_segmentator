import os
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension, CppExtension
from distutils.sysconfig import get_config_vars

(opt,) = get_config_vars("OPT")
os.environ["OPT"] = " ".join(
    flag for flag in opt.split() if flag != "-Wstrict-prototypes"
)

src = "src"
sources = [
    os.path.join(root, file)
    for root, dirs, files in os.walk(src)
    for file in files
    if file.endswith(".cpp") or file.endswith(".cu")
]

setup(
    ext_modules=[
        CppExtension(
            name='libsegmentator._C',
            sources=sources,
            extra_compile_args=['-std=c++17'],
        )
    ],
    cmdclass={"build_ext": BuildExtension},
)