# Source Generated with Decompyle++
# File: cpython-311-c0890f534ec4.pyc (Python 3.11)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(repr(dict.items), "<method 'items' of 'dict' objects>")
    
    class C:
        
        def foo(cls):
            pass


    x = staticmethod(C.foo)
    self.assertEqual(repr(x), f'''<staticmethod({C.foo!r})>''')
    x = classmethod(C.foo)
    self.assertEqual(repr(x), f'''<classmethod({C.foo!r})>''')

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
# WARNING: Decompyle incomplete
