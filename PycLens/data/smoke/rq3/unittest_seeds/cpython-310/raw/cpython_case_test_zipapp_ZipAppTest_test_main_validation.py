# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipapp.py
# case: ZipAppTest_test_main_validation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = self.tmpdir / 'source'
    source.mkdir()
    target = self.tmpdir / 'source.pyz'
    problems = ['', 'foo', 'foo:', ':bar', '12:bar', 'a.b.c.:d', '.a:b', 'a:b.', 'a:.b', 'a:silly name']
    for main in problems:
        with self.subTest(main=main):
            with self.assertRaises(zipapp.ZipAppError):
                zipapp.create_archive(str(source), str(target), main=main)
