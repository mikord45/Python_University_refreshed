def catch_all(f1, f2):
    try:
        print(f1())
    except:
        print(f2())
    print("done")

catch_all(lambda: 10/5, lambda: 'wyjątek')
catch_all(lambda: 10/0, lambda: 'wyjątek')


import sys
# exc_class, exception, exc_traceback = catch_all(lambda: 10 / 0, sys.exec_info)
# print(exc_class)
# print(exception)
# print(exc_traceback)

# import traceback
# error_msg = catch_all(lambda: 10/0, traceback.format_exec)

# for x in range(5):
#     print('iteracja', x)
#     try:
#         while True: pass
#     except Exception: pass
# Naciśnij 5 razy Ctrl+C

s = 'kot'
assert s[0] == 'k'
# assert s[1] == 'k'
assert True
# assert False
# raise ValueError
# raise ValueError()
err = ValueError('error1', 'error2', 'error3')
print(err)
err2 = ValueError('error4')
print(err2)
# raise err2
# raise err
print(err.args)

class SpecialException(Exception): pass

# raise SpecialException('test123', 'test456')
# raise SpecialException()
# raise SpecialException