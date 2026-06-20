# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: ClassCreationTests_test_new_class_metaclass_keywords

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def meta_func(name, bases, ns, **kw):
        return (name, bases, ns, kw)
    res = types.new_class('X', (int, object), dict(metaclass=meta_func, x=0))
    self.assertEqual(res, ('X', (int, object), {}, {'x': 0}))
