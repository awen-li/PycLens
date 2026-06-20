# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {}
    self.assertEqual(repr(d), '{}')
    d[1] = 2
    self.assertEqual(repr(d), '{1: 2}')
    d = {}
    d[1] = d
    self.assertEqual(repr(d), '{1: {...}}')

    class Exc(Exception):
        pass

    class BadRepr(object):

        def __repr__(self):
            raise Exc()
    d = {1: BadRepr()}
    self.assertRaises(Exc, repr, d)
