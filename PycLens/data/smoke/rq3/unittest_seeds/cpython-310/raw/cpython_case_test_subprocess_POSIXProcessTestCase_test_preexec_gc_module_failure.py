# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_preexec_gc_module_failure

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    enabled = gc.isenabled()
    try:
        gc.disable()
        self.assertFalse(gc.isenabled())
        subprocess.call([sys.executable, '-c', ''], preexec_fn=lambda : None)
        self.assertFalse(gc.isenabled(), "Popen enabled gc when it shouldn't.")
        gc.enable()
        self.assertTrue(gc.isenabled())
        subprocess.call([sys.executable, '-c', ''], preexec_fn=lambda : None)
        self.assertTrue(gc.isenabled(), 'Popen left gc disabled.')
    finally:
        if not enabled:
            gc.disable()
