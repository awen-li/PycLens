# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestRmTree_test_rmtree_works_on_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tmp = self.mkdtemp()
    victim = os.path.join(tmp, 'killme')
    os.mkdir(victim)
    write_file(os.path.join(victim, 'somefile'), 'foo')
    victim = os.fsencode(victim)
    self.assertIsInstance(victim, bytes)
    shutil.rmtree(victim)
