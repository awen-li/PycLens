# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: RunStringTests_test_create_thread

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    subinterp = interpreters.create(isolated=False)
    (script, file) = _captured_script("\n            import threading\n            def f():\n                print('it worked!', end='')\n\n            t = threading.Thread(target=f)\n            t.start()\n            t.join()\n            ")
    with file:
        interpreters.run_string(subinterp, script)
        out = file.read()
    self.assertEqual(out, 'it worked!')
