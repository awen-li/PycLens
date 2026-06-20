# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: RunStringTests_test_shared_overwrites

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    interpreters.run_string(self.id, dedent("\n            spam = 'eggs'\n            ns1 = dict(vars())\n            del ns1['__builtins__']\n            "))
    shared = {'spam': b'ham'}
    script = dedent(f"\n            ns2 = dict(vars())\n            del ns2['__builtins__']\n        ")
    interpreters.run_string(self.id, script, shared)
    (r, w) = os.pipe()
    script = dedent(f"\n            ns = dict(vars())\n            del ns['__builtins__']\n            import pickle\n            with open({w}, 'wb') as chan:\n                pickle.dump(ns, chan)\n            ")
    interpreters.run_string(self.id, script)
    with open(r, 'rb') as chan:
        ns = pickle.load(chan)
    self.assertEqual(ns['ns1']['spam'], 'eggs')
    self.assertEqual(ns['ns2']['spam'], b'ham')
    self.assertEqual(ns['spam'], b'ham')
