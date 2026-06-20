# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pickle.py
# case: CompatPickleTests_test_exceptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(mapping('exceptions', 'StandardError'), ('builtins', 'Exception'))
    self.assertEqual(mapping('exceptions', 'Exception'), ('builtins', 'Exception'))
    self.assertEqual(reverse_mapping('builtins', 'Exception'), ('exceptions', 'Exception'))
    self.assertEqual(mapping('exceptions', 'OSError'), ('builtins', 'OSError'))
    self.assertEqual(reverse_mapping('builtins', 'OSError'), ('exceptions', 'OSError'))
    for (name, exc) in get_exceptions(builtins):
        with self.subTest(name):
            if exc in (BlockingIOError, ResourceWarning, StopAsyncIteration, RecursionError, EncodingWarning):
                continue
            if exc is not OSError and issubclass(exc, OSError):
                self.assertEqual(reverse_mapping('builtins', name), ('exceptions', 'OSError'))
            elif exc is not ImportError and issubclass(exc, ImportError):
                self.assertEqual(reverse_mapping('builtins', name), ('exceptions', 'ImportError'))
                self.assertEqual(mapping('exceptions', name), ('exceptions', name))
            else:
                self.assertEqual(reverse_mapping('builtins', name), ('exceptions', name))
                self.assertEqual(mapping('exceptions', name), ('builtins', name))
