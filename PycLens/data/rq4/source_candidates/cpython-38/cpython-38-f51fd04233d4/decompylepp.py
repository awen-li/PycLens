# Source Generated with Decompyle++
# File: cpython-38-f51fd04233d4.pyc (Python 3.8)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    self = None
    __pybcsec_self__ = None
    
    def Evil():
        '''__pybcsec_seed__.<locals>.Evil'''
        
        def __hash__(self):
            return hash('attr')

        
        def __eq__(self, other):
            
            try:
                del C.attr
            finally:
                pass
            except AttributeError:
                pass
            

            return 0


    Evil = None(Evil, 'Evil', object)
    
    class Descr(object):
        __module__ = __name__
        __qualname__ = '__pybcsec_seed__.<locals>.Descr'
    # WARNING: Decompyle incomplete

    
    def C():
        '''__pybcsec_seed__.<locals>.C'''
        attr = Descr()

    C = None(C, 'C', object)
    c = C()
    c.__dict__[Evil()] = 0
    self.assertEqual(c.attr, 1)
    support.gc_collect()
    self.assertNotHasAttr(c, 'attr')

if __name__ == '__main__':
    __pybcsec_seed__()
