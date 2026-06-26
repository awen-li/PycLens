# Source Generated with Decompyle++
# File: cpython-312-71da7692ac83.pyc (Python 3.12)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    actions = []
    
    def make_decorator(tag):
        actions.append('makedec' + tag)
        
        def decorate(func):
            actions.append('calldec' + tag)
            return func

        return decorate

    
    def NameLookupTracer():
        '''__pybcsec_seed__.<locals>.NameLookupTracer'''
        __module__ = __name__
        __qualname__ = '__pybcsec_seed__.<locals>.NameLookupTracer'
        
        def __init__(self, index):
            self.index = index

    # WARNING: Decompyle incomplete

    NameLookupTracer = None(NameLookupTracer, 'NameLookupTracer', object)
    (c1, c2, c3) = map(NameLookupTracer, [
        1,
        2,
        3])
    expected_actions = [
        'evalname1',
        'evalargs1',
        'makedec1',
        'evalname2',
        'evalargs2',
        'makedec2',
        'evalname3',
        'evalargs3',
        'makedec3',
        'calldec3',
        'calldec2',
        'calldec1']
    actions = []
    c3.arg
    foo = (lambda : 42)()()()
    self.assertEqual(foo(), 42)
    self.assertEqual(actions, expected_actions)
    actions = []
    
    def bar():
        return 42

    bar = c1.make_decorator(c1.arg)(c2.make_decorator(c2.arg)(c3.make_decorator(c3.arg)(bar)))
    self.assertEqual(bar(), 42)
    self.assertEqual(actions, expected_actions)

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
