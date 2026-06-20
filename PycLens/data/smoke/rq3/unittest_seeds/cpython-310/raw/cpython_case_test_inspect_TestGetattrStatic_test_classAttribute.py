# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetattrStatic_test_classAttribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Thing(object):
        x = object()
    self.assertEqual(inspect.getattr_static(Thing, 'x'), Thing.x)
