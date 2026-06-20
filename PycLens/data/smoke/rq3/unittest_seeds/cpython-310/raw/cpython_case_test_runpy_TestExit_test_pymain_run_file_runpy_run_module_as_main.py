# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_runpy.py
# case: TestExit_test_pymain_run_file_runpy_run_module_as_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tmp = self.ham.parent
    run_module_as_main = tmp / 'run_module_as_main.py'
    run_module_as_main.write_text(textwrap.dedent('                import runpy\n                runpy._run_module_as_main("ham")\n                '))
    self.assertSigInt([sys.executable, run_module_as_main], cwd=tmp)
