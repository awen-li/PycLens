# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: CreateTests_test_in_threaded_subinterpreter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (main,) = interpreters.list_all()
    id1 = interpreters.create()
    id2 = None

    def f():
        nonlocal id2
        out = _run_output(id1, dedent('\n                import _xxsubinterpreters as _interpreters\n                id = _interpreters.create()\n                print(id)\n                '))
        id2 = int(out.strip())
    t = threading.Thread(target=f)
    t.start()
    t.join()
    self.assertEqual(set(interpreters.list_all()), {main, id1, id2})
