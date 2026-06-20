# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: NameprepTest_test_nameprep

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from encodings.idna import nameprep
    for (pos, (orig, prepped)) in enumerate(nameprep_tests):
        if orig is None:
            continue
        orig = str(orig, 'utf-8', 'surrogatepass')
        if prepped is None:
            self.assertRaises(UnicodeError, nameprep, orig)
        else:
            prepped = str(prepped, 'utf-8', 'surrogatepass')
            try:
                self.assertEqual(nameprep(orig), prepped)
            except Exception as e:
                raise support.TestFailed('Test 3.%d: %s' % (pos + 1, str(e)))
