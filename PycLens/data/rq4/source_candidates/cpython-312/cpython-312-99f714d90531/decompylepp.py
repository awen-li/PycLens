# Source Generated with Decompyle++
# File: cpython-312-99f714d90531.pyc (Python 3.12)


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
        
        def __init__(self, index):
            self.index = index

        
        def __getattr__(self, fname):
            if fname == 'make_decorator':
                res = make_decorator
                opname = 'evalname'
            elif fname == 'arg':
                res = str(self.index)
                opname = 'evalargs'
            else:
                raise 'Unknown attrname %s' % fname()
            actions.append('%s%d' % (opname, self.index))
            return res


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
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
