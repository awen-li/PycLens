# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_name_attribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for cons in self.hash_constructors:
        h = cons(usedforsecurity=False)
        self.assertIsInstance(h.name, str)
        if h.name in self.supported_hash_names:
            self.assertIn(h.name, self.supported_hash_names)
        else:
            self.assertNotIn(h.name, self.supported_hash_names)
        self.assertEqual(h.name, hashlib.new(h.name, usedforsecurity=False).name)
