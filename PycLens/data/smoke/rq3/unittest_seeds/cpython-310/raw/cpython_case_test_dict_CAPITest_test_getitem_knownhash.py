# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: CAPITest_test_getitem_knownhash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import dict_getitem_knownhash
    d = {'x': 1, 'y': 2, 'z': 3}
    self.assertEqual(dict_getitem_knownhash(d, 'x', hash('x')), 1)
    self.assertEqual(dict_getitem_knownhash(d, 'y', hash('y')), 2)
    self.assertEqual(dict_getitem_knownhash(d, 'z', hash('z')), 3)
    self.assertRaises(SystemError, dict_getitem_knownhash, [], 1, hash(1))
    self.assertRaises(KeyError, dict_getitem_knownhash, {}, 1, hash(1))

    class Exc(Exception):
        pass

    class BadEq:

        def __eq__(self, other):
            raise Exc

        def __hash__(self):
            return 7
    (k1, k2) = (BadEq(), BadEq())
    d = {k1: 1}
    self.assertEqual(dict_getitem_knownhash(d, k1, hash(k1)), 1)
    self.assertRaises(Exc, dict_getitem_knownhash, d, k2, hash(k2))
