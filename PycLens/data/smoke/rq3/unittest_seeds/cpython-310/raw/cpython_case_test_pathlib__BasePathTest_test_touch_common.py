# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_touch_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls(BASE)
    p = P / 'newfileA'
    self.assertFalse(p.exists())
    p.touch()
    self.assertTrue(p.exists())
    st = p.stat()
    old_mtime = st.st_mtime
    old_mtime_ns = st.st_mtime_ns
    os.utime(str(p), (old_mtime - 10, old_mtime - 10))
    p.touch()
    st = p.stat()
    self.assertGreaterEqual(st.st_mtime_ns, old_mtime_ns)
    self.assertGreaterEqual(st.st_mtime, old_mtime)
    p = P / 'newfileB'
    self.assertFalse(p.exists())
    p.touch(mode=448, exist_ok=False)
    self.assertTrue(p.exists())
    self.assertRaises(OSError, p.touch, exist_ok=False)
