# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscReadTestBase_test_fileobj_with_offset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tar = tarfile.open(self.tarname, mode=self.mode)
    try:
        tar.next()
        t = tar.next()
        name = t.name
        offset = t.offset
        with tar.extractfile(t) as f:
            data = f.read()
    finally:
        tar.close()
    with self.open(self.tarname) as fobj:
        fobj.seek(offset)
        with tar.open(self.tarname, mode='r:', fileobj=fobj) as tar:
            t = tar.next()
            self.assertEqual(t.name, name)
            tar.getmembers()
            self.assertEqual(tar.extractfile(t).read(), data, 'seek back did not work')
