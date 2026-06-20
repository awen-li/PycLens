# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: DestroyTests_test_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (main,) = interpreters.list_all()
    with self.assertRaises(RuntimeError):
        interpreters.destroy(main)

    def f():
        with self.assertRaises(RuntimeError):
            interpreters.destroy(main)
    t = threading.Thread(target=f)
    t.start()
    t.join()
