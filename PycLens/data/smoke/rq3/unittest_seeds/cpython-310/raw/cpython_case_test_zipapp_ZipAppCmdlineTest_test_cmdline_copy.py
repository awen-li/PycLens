# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipapp.py
# case: ZipAppCmdlineTest_test_cmdline_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    original = self.make_archive()
    target = self.tmpdir / 'target.pyz'
    args = [str(original), '-o', str(target)]
    zipapp.main(args)
    self.assertTrue(target.is_file())
