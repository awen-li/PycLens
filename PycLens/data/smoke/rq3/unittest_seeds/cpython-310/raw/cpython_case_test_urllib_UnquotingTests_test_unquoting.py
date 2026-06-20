# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: UnquotingTests_test_unquoting

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    escape_list = []
    for num in range(128):
        given = hexescape(chr(num))
        expect = chr(num)
        result = urllib.parse.unquote(given)
        self.assertEqual(expect, result, 'using unquote(): %r != %r' % (expect, result))
        result = urllib.parse.unquote_plus(given)
        self.assertEqual(expect, result, 'using unquote_plus(): %r != %r' % (expect, result))
        escape_list.append(given)
    escape_string = ''.join(escape_list)
    del escape_list
    result = urllib.parse.unquote(escape_string)
    self.assertEqual(result.count('%'), 1, 'using unquote(): not all characters escaped: %s' % result)
    self.assertRaises((TypeError, AttributeError), urllib.parse.unquote, None)
    self.assertRaises((TypeError, AttributeError), urllib.parse.unquote, ())
