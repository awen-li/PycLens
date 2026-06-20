# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartialC_test_attributes_unwritable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.partial(capture, 1, 2, a=10, b=20)
    self.assertRaises(AttributeError, setattr, p, 'func', map)
    self.assertRaises(AttributeError, setattr, p, 'args', (1, 2))
    self.assertRaises(AttributeError, setattr, p, 'keywords', dict(a=1, b=2))
    p = self.partial(hex)
    try:
        del p.__dict__
    except TypeError:
        pass
    else:
        self.fail('partial object allowed __dict__ to be deleted')
