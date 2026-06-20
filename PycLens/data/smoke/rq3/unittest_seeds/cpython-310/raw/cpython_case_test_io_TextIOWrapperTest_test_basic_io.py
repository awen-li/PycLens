# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_basic_io

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for chunksize in (1, 2, 3, 4, 5, 15, 16, 17, 31, 32, 33, 63, 64, 65):
        for enc in ('ascii', 'latin-1', 'utf-8'):
            f = self.open(os_helper.TESTFN, 'w+', encoding=enc)
            f._CHUNK_SIZE = chunksize
            self.assertEqual(f.write('abc'), 3)
            f.close()
            f = self.open(os_helper.TESTFN, 'r+', encoding=enc)
            f._CHUNK_SIZE = chunksize
            self.assertEqual(f.tell(), 0)
            self.assertEqual(f.read(), 'abc')
            cookie = f.tell()
            self.assertEqual(f.seek(0), 0)
            self.assertEqual(f.read(None), 'abc')
            f.seek(0)
            self.assertEqual(f.read(2), 'ab')
            self.assertEqual(f.read(1), 'c')
            self.assertEqual(f.read(1), '')
            self.assertEqual(f.read(), '')
            self.assertEqual(f.tell(), cookie)
            self.assertEqual(f.seek(0), 0)
            self.assertEqual(f.seek(0, 2), cookie)
            self.assertEqual(f.write('def'), 3)
            self.assertEqual(f.seek(cookie), cookie)
            self.assertEqual(f.read(), 'def')
            if enc.startswith('utf'):
                self.multi_line_test(f, enc)
            f.close()
