# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_bytes_wrap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(pprint.pformat(b'', width=1), "b''")
    self.assertEqual(pprint.pformat(b'abcd', width=1), "b'abcd'")
    letters = b'abcdefghijklmnopqrstuvwxyz'
    self.assertEqual(pprint.pformat(letters, width=29), repr(letters))
    self.assertEqual(pprint.pformat(letters, width=19), "(b'abcdefghijkl'\n b'mnopqrstuvwxyz')")
    self.assertEqual(pprint.pformat(letters, width=18), "(b'abcdefghijkl'\n b'mnopqrstuvwx'\n b'yz')")
    self.assertEqual(pprint.pformat(letters, width=16), "(b'abcdefghijkl'\n b'mnopqrstuvwx'\n b'yz')")
    special = bytes(range(16))
    self.assertEqual(pprint.pformat(special, width=61), repr(special))
    self.assertEqual(pprint.pformat(special, width=48), "(b'\\x00\\x01\\x02\\x03\\x04\\x05\\x06\\x07\\x08\\t\\n\\x0b'\n b'\\x0c\\r\\x0e\\x0f')")
    self.assertEqual(pprint.pformat(special, width=32), "(b'\\x00\\x01\\x02\\x03'\n b'\\x04\\x05\\x06\\x07\\x08\\t\\n\\x0b'\n b'\\x0c\\r\\x0e\\x0f')")
    self.assertEqual(pprint.pformat(special, width=1), "(b'\\x00\\x01\\x02\\x03'\n b'\\x04\\x05\\x06\\x07'\n b'\\x08\\t\\n\\x0b'\n b'\\x0c\\r\\x0e\\x0f')")
    self.assertEqual(pprint.pformat({'a': 1, 'b': letters, 'c': 2}, width=21), "{'a': 1,\n 'b': b'abcdefghijkl'\n      b'mnopqrstuvwx'\n      b'yz',\n 'c': 2}")
    self.assertEqual(pprint.pformat({'a': 1, 'b': letters, 'c': 2}, width=20), "{'a': 1,\n 'b': b'abcdefgh'\n      b'ijklmnop'\n      b'qrstuvwxyz',\n 'c': 2}")
    self.assertEqual(pprint.pformat([[[[[[letters]]]]]], width=25), "[[[[[[b'abcdefghijklmnop'\n      b'qrstuvwxyz']]]]]]")
    self.assertEqual(pprint.pformat([[[[[[special]]]]]], width=41), "[[[[[[b'\\x00\\x01\\x02\\x03\\x04\\x05\\x06\\x07'\n      b'\\x08\\t\\n\\x0b\\x0c\\r\\x0e\\x0f']]]]]]")
    for width in range(1, 64):
        formatted = pprint.pformat(special, width=width)
        self.assertEqual(eval(formatted), special)
        formatted = pprint.pformat([special] * 2, width=width)
        self.assertEqual(eval(formatted), [special] * 2)
