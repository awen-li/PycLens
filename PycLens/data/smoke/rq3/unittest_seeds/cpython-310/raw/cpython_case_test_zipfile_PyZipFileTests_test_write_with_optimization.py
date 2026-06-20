# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: PyZipFileTests_test_write_with_optimization

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import email
    packagedir = os.path.dirname(email.__file__)
    self.requiresWriteAccess(packagedir)
    optlevel = 1 if __debug__ else 0
    ext = '.pyc'
    with TemporaryFile() as t, zipfile.PyZipFile(t, 'w', optimize=optlevel) as zipfp:
        zipfp.writepy(packagedir)
        names = zipfp.namelist()
        self.assertIn('email/__init__' + ext, names)
        self.assertIn('email/mime/text' + ext, names)
