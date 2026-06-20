# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_recursion_normalizing_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = "if 1:\n            import sys\n            from _testinternalcapi import get_recursion_depth\n\n            class MyException(Exception): pass\n\n            def setrecursionlimit(depth):\n                while 1:\n                    try:\n                        sys.setrecursionlimit(depth)\n                        return depth\n                    except RecursionError:\n                        # sys.setrecursionlimit() raises a RecursionError if\n                        # the new recursion limit is too low (issue #25274).\n                        depth += 1\n\n            def recurse(cnt):\n                cnt -= 1\n                if cnt:\n                    recurse(cnt)\n                else:\n                    generator.throw(MyException)\n\n            def gen():\n                f = open(%a, mode='rb', buffering=0)\n                yield\n\n            generator = gen()\n            next(generator)\n            recursionlimit = sys.getrecursionlimit()\n            depth = get_recursion_depth()\n            try:\n                # Upon the last recursive invocation of recurse(),\n                # tstate->recursion_depth is equal to (recursion_limit - 1)\n                # and is equal to recursion_limit when _gen_throw() calls\n                # PyErr_NormalizeException().\n                recurse(setrecursionlimit(depth + 2) - depth)\n            finally:\n                sys.setrecursionlimit(recursionlimit)\n                print('Done.')\n        " % __file__
    (rc, out, err) = script_helper.assert_python_failure('-Wd', '-c', code)
    self.assertEqual(rc, 1)
    self.assertIn(b'RecursionError', err)
    self.assertIn(b'ResourceWarning', err)
    self.assertIn(b'Done.', out)
