# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_seek_bom

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = os_helper.TESTFN
    for charset in ('utf-8-sig', 'utf-16', 'utf-32'):
        with self.open(filename, 'w', encoding=charset) as f:
            f.write('aaa')
            pos = f.tell()
        with self.open(filename, 'r+', encoding=charset) as f:
            f.seek(pos)
            f.write('zzz')
            f.seek(0)
            f.write('bbb')
        with self.open(filename, 'rb') as f:
            self.assertEqual(f.read(), 'bbbzzz'.encode(charset))
