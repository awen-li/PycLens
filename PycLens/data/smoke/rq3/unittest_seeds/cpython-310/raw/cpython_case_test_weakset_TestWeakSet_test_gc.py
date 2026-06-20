# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_gc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = WeakSet((Foo() for i in range(1000)))
    for elem in s:
        elem.cycle = s
        elem.sub = elem
        elem.set = WeakSet([elem])
