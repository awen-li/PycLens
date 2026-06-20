# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ForwardRefTests_test_default_globals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = "class C:\n    def foo(self, a: 'C') -> 'D': pass\nclass D:\n    def bar(self, b: 'D') -> C: pass\n"
    ns = {}
    exec(code, ns)
    hints = get_type_hints(ns['C'].foo)
    self.assertEqual(hints, {'a': ns['C'], 'return': ns['D']})
