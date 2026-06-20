# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericpath.py
# case: TestGenericTest_test_invalid_paths

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for attr in GenericTest.common_attributes:
        if attr == 'commonprefix':
            continue
        func = getattr(self.pathmodule, attr)
        with self.subTest(attr=attr):
            if attr in ('exists', 'isdir', 'isfile'):
                func('/tmp\udfffabcds')
                func(b'/tmp\xffabcds')
                func('/tmp\x00abcds')
                func(b'/tmp\x00abcds')
            else:
                with self.assertRaises((OSError, UnicodeEncodeError)):
                    func('/tmp\udfffabcds')
                with self.assertRaises((OSError, UnicodeDecodeError)):
                    func(b'/tmp\xffabcds')
                with self.assertRaisesRegex(ValueError, 'embedded null'):
                    func('/tmp\x00abcds')
                with self.assertRaisesRegex(ValueError, 'embedded null'):
                    func(b'/tmp\x00abcds')
