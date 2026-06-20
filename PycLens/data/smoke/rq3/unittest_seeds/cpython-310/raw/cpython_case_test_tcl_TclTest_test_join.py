# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tcl.py
# case: TclTest_test_join

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    join = tkinter._join
    tcl = self.interp.tk

    def unpack(s):
        return tcl.call('lindex', s, 0)

    def check(value):
        self.assertEqual(unpack(join([value])), value)
        self.assertEqual(unpack(join([value, 0])), value)
        self.assertEqual(unpack(unpack(join([[value]]))), value)
        self.assertEqual(unpack(unpack(join([[value, 0]]))), value)
        self.assertEqual(unpack(unpack(join([[value], 0]))), value)
        self.assertEqual(unpack(unpack(join([[value, 0], 0]))), value)
    check('')
    check('spam')
    check('sp am')
    check('sp\tam')
    check('sp\nam')
    check(' \t\n')
    check('{spam}')
    check('{sp am}')
    check('"spam"')
    check('"sp am"')
    check('{"spam"}')
    check('"{spam}"')
    check('sp\\am')
    check('"sp\\am"')
    check('"{}" "{}"')
    check('"\\')
    check('"{')
    check('"}')
    check('\n\\')
    check('\n{')
    check('\n}')
    check('\\\n')
    check('{\n')
    check('}\n')
