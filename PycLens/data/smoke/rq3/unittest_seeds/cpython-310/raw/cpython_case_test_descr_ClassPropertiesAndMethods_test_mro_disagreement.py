# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_mro_disagreement

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mro_err_msg = 'Cannot create a consistent method resolution\norder (MRO) for bases '

    def raises(exc, expected, callable, *args):
        try:
            callable(*args)
        except exc as msg:
            if support.check_impl_detail():
                if not str(msg).startswith(expected):
                    self.fail('Message %r, expected %r' % (str(msg), expected))
        else:
            self.fail('Expected %s' % exc)

    class A(object):
        pass

    class B(A):
        pass

    class C(object):
        pass
    raises(TypeError, 'duplicate base class A', type, 'X', (A, A), {})
    raises(TypeError, mro_err_msg, type, 'X', (A, B), {})
    raises(TypeError, mro_err_msg, type, 'X', (A, C, B), {})

    class GridLayout(object):
        pass

    class HorizontalGrid(GridLayout):
        pass

    class VerticalGrid(GridLayout):
        pass

    class HVGrid(HorizontalGrid, VerticalGrid):
        pass

    class VHGrid(VerticalGrid, HorizontalGrid):
        pass
    raises(TypeError, mro_err_msg, type, 'ConfusedGrid', (HVGrid, VHGrid), {})
