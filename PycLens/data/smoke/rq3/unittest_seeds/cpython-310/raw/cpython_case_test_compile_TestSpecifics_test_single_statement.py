# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_single_statement

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.compile_single('1 + 2')
    self.compile_single('\n1 + 2')
    self.compile_single('1 + 2\n')
    self.compile_single('1 + 2\n\n')
    self.compile_single('1 + 2\t\t\n')
    self.compile_single('1 + 2\t\t\n        ')
    self.compile_single('1 + 2 # one plus two')
    self.compile_single('1; 2')
    self.compile_single('import sys; sys')
    self.compile_single('def f():\n   pass')
    self.compile_single('while False:\n   pass')
    self.compile_single('if x:\n   f(x)')
    self.compile_single('if x:\n   f(x)\nelse:\n   g(x)')
    self.compile_single('class T:\n   pass')
    self.compile_single("c = '''\na=1\nb=2\nc=3\n'''")
