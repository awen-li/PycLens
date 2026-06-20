# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_invalid_registrations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg_prefix = 'Invalid first argument to `register()`: '
    msg_suffix = '. Use either `@register(some_class)` or plain `@register` on an annotated function.'

    @functools.singledispatch
    def i(arg):
        return 'base'
    with self.assertRaises(TypeError) as exc:

        @i.register(42)
        def _(arg):
            return 'I annotated with a non-type'
    self.assertTrue(str(exc.exception).startswith(msg_prefix + '42'))
    self.assertTrue(str(exc.exception).endswith(msg_suffix))
    with self.assertRaises(TypeError) as exc:

        @i.register
        def _(arg):
            return 'I forgot to annotate'
    self.assertTrue(str(exc.exception).startswith(msg_prefix + '<function TestSingleDispatch.test_invalid_registrations.<locals>._'))
    self.assertTrue(str(exc.exception).endswith(msg_suffix))
    with self.assertRaises(TypeError) as exc:

        @i.register
        def _(arg: typing.Iterable[str]):
            return 'I annotated with a generic collection'
    self.assertTrue(str(exc.exception).startswith("Invalid annotation for 'arg'."))
    self.assertTrue(str(exc.exception).endswith('typing.Iterable[str] is not a class.'))
