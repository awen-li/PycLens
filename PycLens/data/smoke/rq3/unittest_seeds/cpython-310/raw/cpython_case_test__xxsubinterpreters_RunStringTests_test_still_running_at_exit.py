# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: RunStringTests_test_still_running_at_exit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = dedent(f"\n        from textwrap import dedent\n        import threading\n        import _xxsubinterpreters as _interpreters\n        id = _interpreters.create()\n        def f():\n            _interpreters.run_string(id, dedent('''\n                import time\n                # Give plenty of time for the main interpreter to finish.\n                time.sleep(1_000_000)\n                '''))\n\n        t = threading.Thread(target=f)\n        t.start()\n        ")
    with support.temp_dir() as dirname:
        filename = script_helper.make_script(dirname, 'interp', script)
        with script_helper.spawn_python(filename) as proc:
            retcode = proc.wait()
    self.assertEqual(retcode, 0)
