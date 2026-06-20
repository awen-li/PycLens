# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_from_iterable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test(range(256))
    self.assertEqual(len(b), 256)
    self.assertEqual(list(b), list(range(256)))
    b = self.type2test({42})
    self.assertEqual(b, b'*')
    b = self.type2test({43, 45})
    self.assertIn(tuple(b), {(43, 45), (45, 43)})
    b = self.type2test(iter(range(256)))
    self.assertEqual(len(b), 256)
    self.assertEqual(list(b), list(range(256)))
    b = self.type2test((i for i in range(256) if i % 2))
    self.assertEqual(len(b), 128)
    self.assertEqual(list(b), list(range(256))[1::2])

    class S:

        def __getitem__(self, i):
            return (1, 2, 3)[i]
    b = self.type2test(S())
    self.assertEqual(b, b'\x01\x02\x03')
