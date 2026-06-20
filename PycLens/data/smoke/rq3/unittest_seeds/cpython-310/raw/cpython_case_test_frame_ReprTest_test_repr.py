# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_frame.py
# case: ReprTest_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def outer():
        x = 5
        y = 6

        def inner():
            z = x + 2
            1 / 0
            t = 9
        return inner()
    offset = outer.__code__.co_firstlineno
    try:
        outer()
    except ZeroDivisionError as e:
        tb = e.__traceback__
        frames = []
        while tb:
            frames.append(tb.tb_frame)
            tb = tb.tb_next
    else:
        self.fail('should have raised')
    (f_this, f_outer, f_inner) = frames
    file_repr = re.escape(repr(__file__))
    self.assertRegex(repr(f_this), '^<frame at 0x[0-9a-fA-F]+, file %s, line %d, code test_repr>$' % (file_repr, offset + 23))
    self.assertRegex(repr(f_outer), '^<frame at 0x[0-9a-fA-F]+, file %s, line %d, code outer>$' % (file_repr, offset + 7))
    self.assertRegex(repr(f_inner), '^<frame at 0x[0-9a-fA-F]+, file %s, line %d, code inner>$' % (file_repr, offset + 5))
