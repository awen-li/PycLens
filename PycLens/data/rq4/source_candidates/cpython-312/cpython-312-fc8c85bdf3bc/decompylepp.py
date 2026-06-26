# Source Generated with Decompyle++
# File: cpython-312-fc8c85bdf3bc.pyc (Python 3.12)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rb_call_count = 0
    
    def B():
        '''__pybcsec_seed__.<locals>.B'''
        
        def __buffer__(self, flags):
            return self(flags)

        
        def __release_buffer__(self, view):
            rb_call_count += 1
            self(view)

        __classcell__ = None

    B = None(B, 'B', bytearray)
    b = B(b'hello')
    mv = memoryview(b)
    self.assertEqual(mv.tobytes(), b'hello')
    self.assertEqual(rb_call_count, 0)
    None(None, None)
    self.assertEqual(rb_call_count, 1)
    return None
    if None:
        pass
    with None:
        if not None:
            pass
    continue

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
