# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_join

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.type2test(b'').join([]), b'')
    self.assertEqual(self.type2test(b'').join([b'']), b'')
    for lst in [[b'abc'], [b'a', b'bc'], [b'ab', b'c'], [b'a', b'b', b'c']]:
        lst = list(map(self.type2test, lst))
        self.assertEqual(self.type2test(b'').join(lst), b'abc')
        self.assertEqual(self.type2test(b'').join(tuple(lst)), b'abc')
        self.assertEqual(self.type2test(b'').join(iter(lst)), b'abc')
    dot_join = self.type2test(b'.:').join
    self.assertEqual(dot_join([b'ab', b'cd']), b'ab.:cd')
    self.assertEqual(dot_join([memoryview(b'ab'), b'cd']), b'ab.:cd')
    self.assertEqual(dot_join([b'ab', memoryview(b'cd')]), b'ab.:cd')
    self.assertEqual(dot_join([bytearray(b'ab'), b'cd']), b'ab.:cd')
    self.assertEqual(dot_join([b'ab', bytearray(b'cd')]), b'ab.:cd')
    seq = [b'abc'] * 100000
    expected = b'abc' + b'.:abc' * 99999
    self.assertEqual(dot_join(seq), expected)
    seq = [b'abc'] * 100000
    expected = b'abc' * 100000
    self.assertEqual(self.type2test(b'').join(seq), expected)
    self.assertRaises(TypeError, self.type2test(b' ').join, None)
    with self.assertRaises(TypeError):
        dot_join([bytearray(b'ab'), 'cd', b'ef'])
    with self.assertRaises(TypeError):
        dot_join([memoryview(b'ab'), 'cd', b'ef'])
