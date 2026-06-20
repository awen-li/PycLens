# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: RunStringTests_test_shared_overwrites_default_vars

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (r, w) = os.pipe()
    shared = {'__name__': b'not __main__'}
    script = dedent(f"\n            spam = 42\n\n            ns = dict(vars())\n            del ns['__builtins__']\n            import pickle\n            with open({w}, 'wb') as chan:\n                pickle.dump(ns, chan)\n            ")
    interpreters.run_string(self.id, script, shared)
    with open(r, 'rb') as chan:
        ns = pickle.load(chan)
    self.assertEqual(ns['__name__'], b'not __main__')
