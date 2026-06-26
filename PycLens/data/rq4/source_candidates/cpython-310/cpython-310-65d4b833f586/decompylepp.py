# Source Generated with Decompyle++
# File: cpython-310-65d4b833f586.pyc (Python 3.10)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sentinel = object()
    
    def f():
        nonlocal_var = None
        
        def g():
            (lambda .0: [ nonlocal_var = sentinel for _ in .0 ])(range(1))

        g()
        self.assertEqual(nonlocal_var, sentinel)

    f()

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
