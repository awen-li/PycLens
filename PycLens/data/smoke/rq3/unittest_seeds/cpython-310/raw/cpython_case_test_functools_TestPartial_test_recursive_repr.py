# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_recursive_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if self.partial in (c_functools.partial, py_functools.partial):
        name = 'functools.partial'
    else:
        name = self.partial.__name__
    f = self.partial(capture)
    f.__setstate__((f, (), {}, {}))
    try:
        self.assertEqual(repr(f), '%s(...)' % (name,))
    finally:
        f.__setstate__((capture, (), {}, {}))
    f = self.partial(capture)
    f.__setstate__((capture, (f,), {}, {}))
    try:
        self.assertEqual(repr(f), '%s(%r, ...)' % (name, capture))
    finally:
        f.__setstate__((capture, (), {}, {}))
    f = self.partial(capture)
    f.__setstate__((capture, (), {'a': f}, {}))
    try:
        self.assertEqual(repr(f), '%s(%r, a=...)' % (name, capture))
    finally:
        f.__setstate__((capture, (), {}, {}))
