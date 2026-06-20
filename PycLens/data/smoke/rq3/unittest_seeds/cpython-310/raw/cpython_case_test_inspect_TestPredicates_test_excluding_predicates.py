# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestPredicates_test_excluding_predicates

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    global tb
    self.istest(inspect.isbuiltin, 'sys.exit')
    self.istest(inspect.isbuiltin, '[].append')
    self.istest(inspect.iscode, 'mod.spam.__code__')
    try:
        1 / 0
    except Exception as e:
        tb = e.__traceback__
        self.istest(inspect.isframe, 'tb.tb_frame')
        self.istest(inspect.istraceback, 'tb')
        if hasattr(types, 'GetSetDescriptorType'):
            self.istest(inspect.isgetsetdescriptor, 'type(tb.tb_frame).f_locals')
        else:
            self.assertFalse(inspect.isgetsetdescriptor(type(tb.tb_frame).f_locals))
    finally:
        tb = None
    self.istest(inspect.isfunction, 'mod.spam')
    self.istest(inspect.isfunction, 'mod.StupidGit.abuse')
    self.istest(inspect.ismethod, 'git.argue')
    self.istest(inspect.ismethod, 'mod.custom_method')
    self.istest(inspect.ismodule, 'mod')
    self.istest(inspect.isdatadescriptor, 'collections.defaultdict.default_factory')
    self.istest(inspect.isgenerator, '(x for x in range(2))')
    self.istest(inspect.isgeneratorfunction, 'generator_function_example')
    self.istest(inspect.isasyncgen, 'async_generator_function_example(1)')
    self.istest(inspect.isasyncgenfunction, 'async_generator_function_example')
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        self.istest(inspect.iscoroutine, 'coroutine_function_example(1)')
        self.istest(inspect.iscoroutinefunction, 'coroutine_function_example')
    if hasattr(types, 'MemberDescriptorType'):
        self.istest(inspect.ismemberdescriptor, 'datetime.timedelta.days')
    else:
        self.assertFalse(inspect.ismemberdescriptor(datetime.timedelta.days))
