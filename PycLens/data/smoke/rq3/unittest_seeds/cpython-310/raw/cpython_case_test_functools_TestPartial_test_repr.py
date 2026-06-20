# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    args = (object(), object())
    args_repr = ', '.join((repr(a) for a in args))
    kwargs = {'a': object(), 'b': object()}
    kwargs_reprs = ['a={a!r}, b={b!r}'.format_map(kwargs), 'b={b!r}, a={a!r}'.format_map(kwargs)]
    if self.partial in (c_functools.partial, py_functools.partial):
        name = 'functools.partial'
    else:
        name = self.partial.__name__
    f = self.partial(capture)
    self.assertEqual(f'{name}({capture!r})', repr(f))
    f = self.partial(capture, *args)
    self.assertEqual(f'{name}({capture!r}, {args_repr})', repr(f))
    f = self.partial(capture, **kwargs)
    self.assertIn(repr(f), [f'{name}({capture!r}, {kwargs_repr})' for kwargs_repr in kwargs_reprs])
    f = self.partial(capture, *args, **kwargs)
    self.assertIn(repr(f), [f'{name}({capture!r}, {args_repr}, {kwargs_repr})' for kwargs_repr in kwargs_reprs])
