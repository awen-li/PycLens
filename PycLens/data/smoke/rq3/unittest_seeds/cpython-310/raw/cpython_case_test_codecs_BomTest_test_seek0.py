# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: BomTest_test_seek0

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = '1234567890'
    tests = ('utf-16', 'utf-16-le', 'utf-16-be', 'utf-32', 'utf-32-le', 'utf-32-be')
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    for encoding in tests:
        with codecs.open(os_helper.TESTFN, 'w+', encoding=encoding) as f:
            f.write(data)
            f.write(data)
            f.seek(0)
            self.assertEqual(f.read(), data * 2)
            f.seek(0)
            self.assertEqual(f.read(), data * 2)
        with codecs.open(os_helper.TESTFN, 'w+', encoding=encoding) as f:
            f.write(data[0])
            self.assertNotEqual(f.tell(), 0)
            f.seek(0)
            f.write(data)
            f.seek(0)
            self.assertEqual(f.read(), data)
        with codecs.open(os_helper.TESTFN, 'w+', encoding=encoding) as f:
            f.writer.write(data[0])
            self.assertNotEqual(f.writer.tell(), 0)
            f.writer.seek(0)
            f.writer.write(data)
            f.seek(0)
            self.assertEqual(f.read(), data)
        with codecs.open(os_helper.TESTFN, 'w+', encoding=encoding) as f:
            f.write(data)
            f.seek(f.tell())
            f.write(data)
            f.seek(0)
            self.assertEqual(f.read(), data * 2)
        with codecs.open(os_helper.TESTFN, 'w+', encoding=encoding) as f:
            f.writer.write(data)
            f.writer.seek(f.writer.tell())
            f.writer.write(data)
            f.seek(0)
            self.assertEqual(f.read(), data * 2)
