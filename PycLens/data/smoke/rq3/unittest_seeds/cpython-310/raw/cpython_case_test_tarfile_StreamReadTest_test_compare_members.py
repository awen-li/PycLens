# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: StreamReadTest_test_compare_members

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tar1 = tarfile.open(tarname, encoding='iso8859-1')
    try:
        tar2 = self.tar
        while True:
            t1 = tar1.next()
            t2 = tar2.next()
            if t1 is None:
                break
            self.assertIsNotNone(t2, 'stream.next() failed.')
            if t2.islnk() or t2.issym():
                with self.assertRaises(tarfile.StreamError):
                    tar2.extractfile(t2)
                continue
            v1 = tar1.extractfile(t1)
            v2 = tar2.extractfile(t2)
            if v1 is None:
                continue
            self.assertIsNotNone(v2, 'stream.extractfile() failed')
            self.assertEqual(v1.read(), v2.read(), 'stream extraction failed')
    finally:
        tar1.close()
