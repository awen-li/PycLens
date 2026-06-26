# Source Generated with Decompyle++
# File: cpython-38-46a59a1a86c9.pyc (Python 3.8)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    args = (object(), object())
    args_repr = ', '.join((lambda .0: for a in .0:
repr(a))(args))
    kwargs = {
        'a': object(),
        'b': object() }
    kwargs_reprs = [
        None(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'a={a!r}, b={b!r}'.format_map, kwargs),
        'b={b!r}, a={a!r}'.format_map(kwargs)]
    if self.partial in (c_functools.partial, py_functools.partial):
        name = 'functools.partial'
    else:
        name = self.partial.__name__
    f = self.partial(capture)
    self.assertEqual(f'''{name}({capture!r})''', repr(f))
    f = self.partial(<NODE:0>)
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    __pybcsec_seed__()
