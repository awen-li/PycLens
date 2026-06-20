# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ExternalTests_test_re_tests

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from test.re_tests import tests, FAIL, SYNTAX_ERROR
    for t in tests:
        pattern = s = outcome = repl = expected = None
        if len(t) == 5:
            (pattern, s, outcome, repl, expected) = t
        elif len(t) == 3:
            (pattern, s, outcome) = t
        else:
            raise ValueError('Test tuples should have 3 or 5 fields', t)
        with self.subTest(pattern=pattern, string=s):
            if outcome == SYNTAX_ERROR:
                with self.assertRaises(re.error):
                    re.compile(pattern)
                continue
            obj = re.compile(pattern)
            result = obj.search(s)
            if outcome == FAIL:
                self.assertIsNone(result, 'Succeeded incorrectly')
                continue
            with self.subTest():
                self.assertTrue(result, 'Failed incorrectly')
                (start, end) = result.span(0)
                vardict = {'found': result.group(0), 'groups': result.group(), 'flags': result.re.flags}
                for i in range(1, 100):
                    try:
                        gi = result.group(i)
                        if gi is None:
                            gi = 'None'
                    except IndexError:
                        gi = 'Error'
                    vardict['g%d' % i] = gi
                for i in result.re.groupindex.keys():
                    try:
                        gi = result.group(i)
                        if gi is None:
                            gi = 'None'
                    except IndexError:
                        gi = 'Error'
                    vardict[i] = gi
                self.assertEqual(eval(repl, vardict), expected, 'grouping error')
            try:
                bpat = bytes(pattern, 'ascii')
                bs = bytes(s, 'ascii')
            except UnicodeEncodeError:
                pass
            else:
                with self.subTest('bytes pattern match'):
                    obj = re.compile(bpat)
                    self.assertTrue(obj.search(bs))
                with self.subTest('locale-sensitive match'):
                    obj = re.compile(bpat, re.LOCALE)
                    result = obj.search(bs)
                    if result is None:
                        print('=== Fails on locale-sensitive match', t)
            if pattern[:2] != '\\B' and pattern[-2:] != '\\B' and (result is not None):
                with self.subTest('range-limited match'):
                    obj = re.compile(pattern)
                    self.assertTrue(obj.search(s, start, end + 1))
            with self.subTest('case-insensitive match'):
                obj = re.compile(pattern, re.IGNORECASE)
                self.assertTrue(obj.search(s))
            with self.subTest('unicode-sensitive match'):
                obj = re.compile(pattern, re.UNICODE)
                self.assertTrue(obj.search(s))
