# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestUpdateWrapper_test_no_update

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        """This is a test"""
        pass
    f.attr = 'This is also a test'

    def wrapper():
        pass
    functools.update_wrapper(wrapper, f, (), ())
    self.check_wrapper(wrapper, f, (), ())
    self.assertEqual(wrapper.__name__, 'wrapper')
    self.assertNotEqual(wrapper.__qualname__, f.__qualname__)
    self.assertEqual(wrapper.__doc__, None)
    self.assertEqual(wrapper.__annotations__, {})
    self.assertFalse(hasattr(wrapper, 'attr'))
