# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: AsyncBadSyntaxTest_test_badsyntax_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    samples = ['def foo():\n                await = 1\n            ', 'class Bar:\n                def async(): pass\n            ', 'class Bar:\n                async = 1\n            ', 'class async:\n                pass\n            ', 'class await:\n                pass\n            ', 'import math as await', 'def async():\n                pass', 'def foo(*, await=1):\n                passasync = 1', 'print(await=1)']
    for code in samples:
        with self.subTest(code=code), self.assertRaises(SyntaxError):
            compile(code, '<test>', 'exec')
