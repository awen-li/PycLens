# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_recursion_in_except_handler

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def set_relative_recursion_limit(n):
        depth = 1
        while True:
            try:
                sys.setrecursionlimit(depth)
            except RecursionError:
                depth += 1
            else:
                break
        sys.setrecursionlimit(depth + n)

    def recurse_in_except():
        try:
            1 / 0
        except:
            recurse_in_except()

    def recurse_after_except():
        try:
            1 / 0
        except:
            pass
        recurse_after_except()

    def recurse_in_body_and_except():
        try:
            recurse_in_body_and_except()
        except:
            recurse_in_body_and_except()
    recursionlimit = sys.getrecursionlimit()
    try:
        set_relative_recursion_limit(10)
        for func in (recurse_in_except, recurse_after_except, recurse_in_body_and_except):
            with self.subTest(func=func):
                try:
                    func()
                except RecursionError:
                    pass
                else:
                    self.fail('Should have raised a RecursionError')
    finally:
        sys.setrecursionlimit(recursionlimit)
