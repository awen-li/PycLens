# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: PyZipFileTests_test_write_pyfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.requiresWriteAccess(os.path.dirname(__file__))
    with TemporaryFile() as t, zipfile.PyZipFile(t, 'w') as zipfp:
        fn = __file__
        if fn.endswith('.pyc'):
            path_split = fn.split(os.sep)
            if os.altsep is not None:
                path_split.extend(fn.split(os.altsep))
            if '__pycache__' in path_split:
                fn = importlib.util.source_from_cache(fn)
            else:
                fn = fn[:-1]
        zipfp.writepy(fn)
        bn = os.path.basename(fn)
        self.assertNotIn(bn, zipfp.namelist())
        self.assertCompiledIn(bn, zipfp.namelist())
    with TemporaryFile() as t, zipfile.PyZipFile(t, 'w') as zipfp:
        fn = __file__
        if fn.endswith('.pyc'):
            fn = fn[:-1]
        zipfp.writepy(fn, 'testpackage')
        bn = '%s/%s' % ('testpackage', os.path.basename(fn))
        self.assertNotIn(bn, zipfp.namelist())
        self.assertCompiledIn(bn, zipfp.namelist())
