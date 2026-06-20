# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestMkstempInner_test_choose_directory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dir = tempfile.mkdtemp()
    try:
        self.do_create(dir=dir).write(b'blat')
        self.do_create(dir=pathlib.Path(dir)).write(b'blat')
    finally:
        support.gc_collect()
        os.rmdir(dir)
