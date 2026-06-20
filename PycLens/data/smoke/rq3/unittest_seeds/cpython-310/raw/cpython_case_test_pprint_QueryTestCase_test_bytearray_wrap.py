# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_bytearray_wrap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(pprint.pformat(bytearray(), width=1), "bytearray(b'')")
    letters = bytearray(b'abcdefghijklmnopqrstuvwxyz')
    self.assertEqual(pprint.pformat(letters, width=40), repr(letters))
    self.assertEqual(pprint.pformat(letters, width=28), "bytearray(b'abcdefghijkl'\n          b'mnopqrstuvwxyz')")
    self.assertEqual(pprint.pformat(letters, width=27), "bytearray(b'abcdefghijkl'\n          b'mnopqrstuvwx'\n          b'yz')")
    self.assertEqual(pprint.pformat(letters, width=25), "bytearray(b'abcdefghijkl'\n          b'mnopqrstuvwx'\n          b'yz')")
    special = bytearray(range(16))
    self.assertEqual(pprint.pformat(special, width=72), repr(special))
    self.assertEqual(pprint.pformat(special, width=57), "bytearray(b'\\x00\\x01\\x02\\x03\\x04\\x05\\x06\\x07\\x08\\t\\n\\x0b'\n          b'\\x0c\\r\\x0e\\x0f')")
    self.assertEqual(pprint.pformat(special, width=41), "bytearray(b'\\x00\\x01\\x02\\x03'\n          b'\\x04\\x05\\x06\\x07\\x08\\t\\n\\x0b'\n          b'\\x0c\\r\\x0e\\x0f')")
    self.assertEqual(pprint.pformat(special, width=1), "bytearray(b'\\x00\\x01\\x02\\x03'\n          b'\\x04\\x05\\x06\\x07'\n          b'\\x08\\t\\n\\x0b'\n          b'\\x0c\\r\\x0e\\x0f')")
    self.assertEqual(pprint.pformat({'a': 1, 'b': letters, 'c': 2}, width=31), "{'a': 1,\n 'b': bytearray(b'abcdefghijkl'\n                b'mnopqrstuvwx'\n                b'yz'),\n 'c': 2}")
    self.assertEqual(pprint.pformat([[[[[letters]]]]], width=37), "[[[[[bytearray(b'abcdefghijklmnop'\n               b'qrstuvwxyz')]]]]]")
    self.assertEqual(pprint.pformat([[[[[special]]]]], width=50), "[[[[[bytearray(b'\\x00\\x01\\x02\\x03\\x04\\x05\\x06\\x07'\n               b'\\x08\\t\\n\\x0b\\x0c\\r\\x0e\\x0f')]]]]]")
