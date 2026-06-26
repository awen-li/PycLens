# Source Generated with Decompyle++
# File: cpython-39-68835a05e586.pyc (Python 3.9)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rebinding = '[x := i for i in range(3) if (x := i) or not x]'
    filter_ref = '[x := i for i in range(3) if x or not x]'
    body_ref = '[x for i in range(3) if (x := i) or not x]'
    nested_ref = '[j for i in range(3) if x or not x for j in range(3) if (x := i)][:-3]'
    cases = [
        ('Rebind global', f'''x = 1; result = {rebinding}'''),
        ('Rebind nonlocal', f'''result, x = (lambda x=1: ({rebinding}, x))()'''),
        ('Filter global', f'''x = 1; result = {filter_ref}'''),
        ('Filter nonlocal', f'''result, x = (lambda x=1: ({filter_ref}, x))()'''),
        ('Body global', f'''x = 1; result = {body_ref}'''),
        ('Body nonlocal', f'''result, x = (lambda x=1: ({body_ref}, x))()'''),
        ('Nested global', f'''x = 1; result = {nested_ref}'''),
        ('Nested nonlocal', f'''result, x = (lambda x=1: ({nested_ref}, x))()''')]
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    __pybcsec_seed__()
