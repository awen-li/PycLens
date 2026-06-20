# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PosixPathTest_test_resolve_root

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    current_directory = os.getcwd()
    try:
        os.chdir('/')
        p = self.cls('spam')
        self.assertEqual(str(p.resolve()), '/spam')
    finally:
        os.chdir(current_directory)
