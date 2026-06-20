# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_runpy.py
# case: TestExit_test_pymain_run_file_runpy_run_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tmp = self.ham.parent
    run_module = tmp / 'run_module.py'
    run_module.write_text(textwrap.dedent('                import runpy\n                runpy.run_module("ham")\n                '))
    self.assertSigInt([sys.executable, run_module], cwd=tmp)
