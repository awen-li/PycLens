# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypeTests_test_type_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class User:
        pass

    class BasicUser(User):
        pass

    class ProUser(User):
        pass

    def new_user(user_class: Type[User]) -> User:
        return user_class()
    new_user(BasicUser)
