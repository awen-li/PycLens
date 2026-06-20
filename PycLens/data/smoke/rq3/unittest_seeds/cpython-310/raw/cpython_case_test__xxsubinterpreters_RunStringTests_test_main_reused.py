# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: RunStringTests_test_main_reused

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (r, w) = os.pipe()
    interpreters.run_string(self.id, dedent(f"\n            spam = True\n\n            ns = dict(vars())\n            del ns['__builtins__']\n            import pickle\n            with open({w}, 'wb') as chan:\n                pickle.dump(ns, chan)\n            del ns, pickle, chan\n            "))
    with open(r, 'rb') as chan:
        ns1 = pickle.load(chan)
    (r, w) = os.pipe()
    interpreters.run_string(self.id, dedent(f"\n            eggs = False\n\n            ns = dict(vars())\n            del ns['__builtins__']\n            import pickle\n            with open({w}, 'wb') as chan:\n                pickle.dump(ns, chan)\n            "))
    with open(r, 'rb') as chan:
        ns2 = pickle.load(chan)
    self.assertIn('spam', ns1)
    self.assertNotIn('eggs', ns1)
    self.assertIn('eggs', ns2)
    self.assertIn('spam', ns2)
