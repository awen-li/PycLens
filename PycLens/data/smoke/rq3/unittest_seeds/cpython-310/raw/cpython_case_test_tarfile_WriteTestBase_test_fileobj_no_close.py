# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: WriteTestBase_test_fileobj_no_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fobj = io.BytesIO()
    with tarfile.open(fileobj=fobj, mode=self.mode) as tar:
        tar.addfile(tarfile.TarInfo('foo'))
    self.assertFalse(fobj.closed, 'external fileobjs must never closed')
    data = fobj.getvalue()
    del tar
    support.gc_collect()
    self.assertFalse(fobj.closed)
    self.assertEqual(data, fobj.getvalue())
