from distutils.core import setup, Extension
# python3 setup.py build_ext --inplace

run_pe_module_module = Extension(
      'run_pe', sources=['RunPE.cpp'],
      language='c++',)

setup(name='RunPE',
      description='A module of RunPE.',
      ext_modules=[run_pe_module_module],
)