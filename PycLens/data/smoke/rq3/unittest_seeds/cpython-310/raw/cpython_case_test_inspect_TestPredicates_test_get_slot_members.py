# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestPredicates_test_get_slot_members

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):
        __slots__ = ('a', 'b')
    x = C()
    x.a = 42
    members = dict(inspect.getmembers(x))
    self.assertIn('a', members)
    self.assertNotIn('b', members)
