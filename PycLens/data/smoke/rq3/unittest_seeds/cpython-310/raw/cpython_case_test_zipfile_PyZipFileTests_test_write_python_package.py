# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: PyZipFileTests_test_write_python_package

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import email
    packagedir = os.path.dirname(email.__file__)
    self.requiresWriteAccess(packagedir)
    with TemporaryFile() as t, zipfile.PyZipFile(t, 'w') as zipfp:
        zipfp.writepy(packagedir)
        names = zipfp.namelist()
        self.assertCompiledIn('email/__init__.py', names)
        self.assertCompiledIn('email/mime/text.py', names)
