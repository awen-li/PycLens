# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestDetectEncoding_test_open

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = os_helper.TESTFN + '.py'
    self.addCleanup(os_helper.unlink, filename)
    for encoding in ('iso-8859-15', 'utf-8'):
        with open(filename, 'w', encoding=encoding) as fp:
            print('# coding: %s' % encoding, file=fp)
            print("print('euro:€')", file=fp)
        with tokenize_open(filename) as fp:
            self.assertEqual(fp.encoding, encoding)
            self.assertEqual(fp.mode, 'r')
    with open(filename, 'w', encoding='utf-8-sig') as fp:
        print("print('euro:€')", file=fp)
    with tokenize_open(filename) as fp:
        self.assertEqual(fp.encoding, 'utf-8-sig')
        self.assertEqual(fp.mode, 'r')
