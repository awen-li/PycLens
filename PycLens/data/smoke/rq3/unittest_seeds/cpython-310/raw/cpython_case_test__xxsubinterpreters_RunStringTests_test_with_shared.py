# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: RunStringTests_test_with_shared

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (r, w) = os.pipe()
    shared = {'spam': b'ham', 'eggs': b'-1', 'cheddar': None}
    script = dedent(f"\n            eggs = int(eggs)\n            spam = 42\n            result = spam + eggs\n\n            ns = dict(vars())\n            del ns['__builtins__']\n            import pickle\n            with open({w}, 'wb') as chan:\n                pickle.dump(ns, chan)\n            ")
    interpreters.run_string(self.id, script, shared)
    with open(r, 'rb') as chan:
        ns = pickle.load(chan)
    self.assertEqual(ns['spam'], 42)
    self.assertEqual(ns['eggs'], -1)
    self.assertEqual(ns['result'], 41)
    self.assertIsNone(ns['cheddar'])
