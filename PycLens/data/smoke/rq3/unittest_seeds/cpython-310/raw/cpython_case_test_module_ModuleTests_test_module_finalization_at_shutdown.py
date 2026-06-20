# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_module.py
# case: ModuleTests_test_module_finalization_at_shutdown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, out, err) = assert_python_ok('-c', 'from test import final_a')
    self.assertFalse(err)
    lines = out.splitlines()
    self.assertEqual(set(lines), {b'x = a', b'x = b', b'final_a.x = a', b'final_b.x = b', b'len = len', b'shutil.rmtree = rmtree'})
