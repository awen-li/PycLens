# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkgutil.py
# case: PkgutilTests_test_name_resolution

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import logging
    import logging.handlers
    success_cases = (('os', os), ('os.path', os.path), ('os.path:pathsep', os.path.pathsep), ('logging', logging), ('logging:', logging), ('logging.handlers', logging.handlers), ('logging.handlers:', logging.handlers), ('logging.handlers:SysLogHandler', logging.handlers.SysLogHandler), ('logging.handlers.SysLogHandler', logging.handlers.SysLogHandler), ('logging.handlers:SysLogHandler.LOG_ALERT', logging.handlers.SysLogHandler.LOG_ALERT), ('logging.handlers.SysLogHandler.LOG_ALERT', logging.handlers.SysLogHandler.LOG_ALERT), ('builtins.int', int), ('builtins:int', int), ('builtins.int.from_bytes', int.from_bytes), ('builtins:int.from_bytes', int.from_bytes), ('builtins.ZeroDivisionError', ZeroDivisionError), ('builtins:ZeroDivisionError', ZeroDivisionError), ('os:path', os.path))
    failure_cases = ((None, TypeError), (1, TypeError), (2.0, TypeError), (True, TypeError), ('', ValueError), ('?abc', ValueError), ('abc/foo', ValueError), ('foo', ImportError), ('os.foo', AttributeError), ('os.foo:', ImportError), ('os.pth:pathsep', ImportError), ('logging.handlers:NoSuchHandler', AttributeError), ('logging.handlers:SysLogHandler.NO_SUCH_VALUE', AttributeError), ('logging.handlers.SysLogHandler.NO_SUCH_VALUE', AttributeError), ('ZeroDivisionError', ImportError), ('os.path.9abc', ValueError), ('9abc', ValueError))
    unicode_words = ('वमस', 'é', 'È', '안녕하세요', 'さよなら', 'ありがとう', 'Хорошо', 'спасибо', '现代汉语常用字表')
    for uw in unicode_words:
        d = os.path.join(self.dirname, uw)
        try:
            os.makedirs(d, exist_ok=True)
        except UnicodeEncodeError:
            continue
        f = os.path.join(d, '__init__.py')
        with open(f, 'w') as f:
            f.write('')
            f.flush()
        importlib.invalidate_caches()
        mod = importlib.import_module(uw)
        success_cases += ((uw, mod),)
        if len(uw) > 1:
            failure_cases += ((uw[:-1], ImportError),)
    failure_cases += (('०वमस', ValueError),)
    for (s, expected) in success_cases:
        with self.subTest(s=s):
            o = pkgutil.resolve_name(s)
            self.assertEqual(o, expected)
    for (s, exc) in failure_cases:
        with self.subTest(s=s):
            with self.assertRaises(exc):
                pkgutil.resolve_name(s)
