# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_badisinstance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Meta(type):

        def __subclasscheck__(cls, subclass):
            raise ValueError()

    class MyException(Exception, metaclass=Meta):
        pass
    with captured_stderr() as stderr:
        try:
            raise KeyError()
        except MyException as e:
            self.fail('exception should not be a MyException')
        except KeyError:
            pass
        except:
            self.fail('Should have raised KeyError')
        else:
            self.fail('Should have raised KeyError')

    def g():
        try:
            return g()
        except RecursionError:
            return sys.exc_info()
    (e, v, tb) = g()
    self.assertIsInstance(v, RecursionError, type(v))
    self.assertIn('maximum recursion depth exceeded', str(v))
