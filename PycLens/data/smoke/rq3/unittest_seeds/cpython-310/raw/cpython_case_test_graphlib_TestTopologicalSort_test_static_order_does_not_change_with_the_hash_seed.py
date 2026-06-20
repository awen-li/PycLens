# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_graphlib.py
# case: TestTopologicalSort_test_static_order_does_not_change_with_the_hash_seed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check_order_with_hash_seed(seed):
        code = "if 1:\n                import graphlib\n                ts = graphlib.TopologicalSorter()\n                ts.add('blech', 'bluch', 'hola')\n                ts.add('abcd', 'blech', 'bluch', 'a', 'b')\n                ts.add('a', 'a string', 'something', 'b')\n                ts.add('bluch', 'hola', 'abcde', 'a', 'b')\n                print(list(ts.static_order()))\n                "
        env = os.environ.copy()
        env['__cleanenv'] = True
        env['PYTHONHASHSEED'] = str(seed)
        out = assert_python_ok('-c', code, **env)
        return out
    run1 = check_order_with_hash_seed(1234)
    run2 = check_order_with_hash_seed(31415)
    self.assertNotEqual(run1, '')
    self.assertNotEqual(run2, '')
    self.assertEqual(run1, run2)
