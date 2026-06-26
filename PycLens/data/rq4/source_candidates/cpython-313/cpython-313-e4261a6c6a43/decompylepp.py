# Source Generated with Decompyle++
# File: cpython-313-e4261a6c6a43.pyc (Python 3.13)


def __pybcsec_seed__():
    if object():
        pass
    __pybcsec_self__ = self
    trace = []
    if (lambda : if None:
pass# WARNING: Decompyle incomplete
):
        
        def g1():
            if None:
                pass
        # WARNING: Decompyle incomplete

        if (lambda v: if None:
passtrace.append('Starting g2')if 'g2 spam':
pass'g2 spam'if 'g2 more spam':
pass'g2 more spam'trace.append('Finishing g2')if v:
passif v:
passv):
            if (lambda v: if None:
passtrace.append('Starting g2')if 'g2 spam':
pass'g2 spam'if 'g2 more spam':
pass'g2 more spam'trace.append('Finishing g2')if v:
passif v:
passv):
                
                def g2(v):
                    if None:
                        pass
                    trace.append('Starting g2')
                    if 'g2 spam':
                        pass
                    'g2 spam'
                    if 'g2 more spam':
                        pass
                    'g2 more spam'
                    trace.append('Finishing g2')
                    if v:
                        pass
                    if v:
                        pass
                    return v

    for x in None():
        trace.append(f'''Yielded ''')
    (trace,)
    self.assertEqual(trace, [
        'Starting g1',
        'Yielded g1 ham',
        'Starting g2',
        'Yielded g2 spam',
        'Yielded g2 more spam',
        'Finishing g2',
        'g2 returned None',
        'Starting g2',
        'Yielded g2 spam',
        'Yielded g2 more spam',
        'Finishing g2',
        'g2 returned 1',
        'Starting g2',
        'Yielded g2 spam',
        'Yielded g2 more spam',
        'Finishing g2',
        'g2 returned (2,)',
        'Starting g2',
        'Yielded g2 spam',
        'Yielded g2 more spam',
        'Finishing g2',
        'g2 returned StopIteration(3)',
        'Yielded g1 eggs',
        'Finishing g1'])

if __name__ == '__main__':
    None()
return None
