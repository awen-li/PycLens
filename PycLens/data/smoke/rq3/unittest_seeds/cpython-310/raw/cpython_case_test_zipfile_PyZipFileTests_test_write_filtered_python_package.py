# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: PyZipFileTests_test_write_filtered_python_package

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import test
    packagedir = os.path.dirname(test.__file__)
    self.requiresWriteAccess(packagedir)
    with TemporaryFile() as t, zipfile.PyZipFile(t, 'w') as zipfp:
        with captured_stdout() as reportSIO:
            zipfp.writepy(packagedir)
        reportStr = reportSIO.getvalue()
        self.assertTrue('SyntaxError' in reportStr)
        with captured_stdout() as reportSIO:
            zipfp.writepy(packagedir, filterfunc=lambda whatever: False)
        reportStr = reportSIO.getvalue()
        self.assertTrue('SyntaxError' not in reportStr)

        def filter(path):
            return not os.path.basename(path).startswith('bad')
        with captured_stdout() as reportSIO, self.assertWarns(UserWarning):
            zipfp.writepy(packagedir, filterfunc=filter)
        reportStr = reportSIO.getvalue()
        if reportStr:
            print(reportStr)
        self.assertTrue('SyntaxError' not in reportStr)
