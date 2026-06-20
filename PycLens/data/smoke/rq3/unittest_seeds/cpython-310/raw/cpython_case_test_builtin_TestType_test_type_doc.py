# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: TestType_test_type_doc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for doc in ('x', 'Ä', '🐍', 'x\x00y', b'x', 42, None):
        A = type('A', (), {'__doc__': doc})
        self.assertEqual(A.__doc__, doc)
    with self.assertRaises(UnicodeEncodeError):
        type('A', (), {'__doc__': 'x\udcdcy'})
    A = type('A', (), {})
    self.assertEqual(A.__doc__, None)
    for doc in ('x', 'Ä', '🐍', 'x\x00y', 'x\udcdcy', b'x', 42, None):
        A.__doc__ = doc
        self.assertEqual(A.__doc__, doc)
