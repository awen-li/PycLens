# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestBadTempdir_test_non_directory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with _inside_empty_temp_dir():
        tempdir = os.path.join(tempfile.tempdir, 'file')
        open(tempdir, 'wb').close()
        with support.swap_attr(tempfile, 'tempdir', tempdir):
            with self.assertRaises((NotADirectoryError, FileNotFoundError)):
                self.make_temp()
