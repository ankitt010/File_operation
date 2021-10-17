# import contextlib
# import functools
# from os import name
# from threading import Thread
# import threading
# from typing import ContextManager

# # # plain decorator
# # '''
# # user_info = {'password':'1234','user':'admin'}


# # import functools
# # def make_secure(func):
# #     @functools.wraps(func)
# #     def secure_function(name):
# #         if user_info['user'] == 'admin':
# #             x = func(name)
# #             return (x, name)
# #         else:
# #              return "access denied"
# #     return secure_function
# # # print(secure_function())


# # @make_secure
# # def get_password(name):
# #     # print()
# #     return 1234

# # # get_password = make_secure(get_password)
# # # print(get_password)
# # print(get_password.__name__)
# # print(get_password('ankit'))
# # '''

# # # custom_iterator using class and genrator
# # '''
# # class Counter():
# #     def __init__(self,low,high):
# #         self.current = low - 1
# #         self.high = high    
# #     def __iter__(self):
# #         return self
# #     def __next__(self):
# #         self.current += 1
# #         if self.current < self.high:
            
# #             return self.current
# #         raise StopIteration

# # # custom iterator using genrator
def counter(low,high):
    while low < high:
        yield low
        low +=1

for c in counter(3,9):
    print(c)
# # # print(counter(3,9))
# # '''
# # # decoratorFunctionWithArguments
# # '''
# # def decoratorFunctionWithArguments(arg1, arg2, arg3):
# #     def wrap(f):
# #         print("Inside wrap()")
# #         @functools.wraps(f)
# #         def wrapped_f(*args):
# #             print("Inside wrapped_f()")
# #             print(f'Decorator arguments: {arg1, arg2, arg3}')
# #             f(*args)
# #             print("After f(*args)")
# #         return wrapped_f
# #     return wrap

# # @decoratorFunctionWithArguments("hello", "world", 42)
# # def sayHello(a1, a2, a3, a4):
# #     print(f'sayHello arguments:{a1, a2, a3, a4}')

# # print(sayHello(1,2,34,43))
# # print(sayHello.__name__)
# # '''
# # # pandas loc and iloc
# # # import pandas as pd
# # # mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
# # #           {'a': 100, 'b': 200, 'c': 300, 'd': 400},
# # #           {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 }]
# # # df = pd.DataFrame(mydict)
# # # print(df)

# # # # custom iterator
# # # def counter(low,high):
# # #     while low < high:
# # #         yield low
# # #         low = low+1
       
# # # for c in counter(3,9):
# # #     print(c)

# # # context manager and custom context amangers
# # # with open ('file.txt','w') as f:
# # #     f.write('my name is ankit')
# # #     # print(f)

# # # import time
# # # from contextlib import contextmanager

# # # @ContextManager
# # # def entry_exit():
# # #     print('entering')
# # #     time.sleep(2)
# # #     print("exiting")

# # # with open(entry_exit) as func:
# # #     func()
# # '''
# # class Open_file():
# #     def __init__(self,file_name,mode):
# #          self.file_name = file_name
# #          self.mode = mode

# #     def __enter__(self):
# #         self.file = open(self.file_name,self.mode)
# #         return self.file

# #     def __exit__(self,execution_type,exec_value,traceback):
# #         self.file.close()

# # with Open_file('file.txt','w') as f:
# #     f.write('ankit singh chandel')

# # print(f.closed)

# # @contextmanager
# # def open_file(file_name,mode):
# #     try:
# #         f = open(file_name,mode)
# #         yield f
# #     finally:
# #         f.close()
# #     # pass
# # with open_file ('custom.txt','w') as f:
# #     f.write("hope you have enjoyed")
# # print(f.closed)

# # import os 
# # cwd = os.getcwd()
# # print(os.listdir())
# # destination = r'C:\Users\ankit.chandel\Desktop\python_handson\code'
# # print(cwd)
# # os.chdir(destination)
# # print(os.listdir())
# # os.chdir(cwd)

# # @contextmanager
# # def change_dir(destination):
# #     try:
# #         cwd = os.getcwd()
# #         os.chdir(destination)
# #         yield
# #     finally:
# #         os.chdir(cwd)
# # with change_dir(destination):
# #     print(os.listdir())
# # '''

# # threading and lock and deadlock and asynico and 
# import concurrent.futures
# import time

# from numpy import number
# def demo_func(timer):
#     print('hello i am entering',)
#     time.sleep(timer)
#     print('I am done')
# print(__name__)
# # if __name__ == '__main__':
# #     with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
# #         executor.map(demo_func,range(10))
# #     thread_list  =[]
# #     for _ in range(10):
# #         t = threading.Thread (target = demo_func,args=(2,))
# #         thread_list.append(t)
# #         t.start()
# #     for thread in thread_list:
# #         thread.join()
 
# #     t = Thread.threading(targ)
# # try and except and else and finally and raise exception

# # inheritance with overriding the constructor
# import logging

# # class FakeDatabase:
# #     def __init__(self):
# #         self.value = 0

# #     def update(self, name):
# #         logging.info("Thread %s: starting update", name)
# #         local_copy = self.value
# #         local_copy += 1     #race condition arises
# #         # self.value = local_copy
# #         time.sleep(0.1)
# #         self.value = local_copy
# #         logging.info("Thread %s: finishing update", name)
# # if __name__ == '__main__':
# #     format = "%(asctime)s: %(message)s"
# #     logging.basicConfig(format=format, level=logging.INFO,
# #                     datefmt="%H:%M:%S")
# #     database = FakeDatabase()
# #     logging.info("Testing update. Ending value is %d.", database.value)
# #     with concurrent.futures.ThreadPoolExecutor(max_workers=100) as exe:
# #         # for index in range(2):
# #         for index in range(2):
# #             exe.submit(database.update,index)
# #     logging.info("Testing update. Ending value is %d.", database.value)

# # import multiprocessing
# # def cpu_bound(number):
# #     return sum(i * i for i in range(number))

# # def sum_number(number):
# #     with multiprocessing.Pool() as pool:
# #         pool.map(cpu_bound,numbers)
# #     # cpu_bound(number)

# # if __name__ == '__main__':
# #     numbers = [5_000_000 + x for x in range(20)]
# #     # numbers = 5000000

# #     start_time = time.time()
# #     sum_number(numbers)
# #     duration = time.time() - start_time
# #     print(f"Duration {duration} seconds")


# import functools  


# # def decorato_with_argument(number,value):
# #     def outer_func(func):
# #         @functools.wraps(func)
# #         def inner_func(*args,**kwargs):
# #             try:
# #                 print(number,value)
# #                 func(*args,**kwargs)
# #                 # print(name)
# #                 print(*args)
# #             except Exception as e:
# #                 print(e)
# #         return inner_func
# #     return outer_func

# # @decorato_with_argument(100,'ankitsingh')
# # def my_func(name):
# #     print(f'my name is {name}')
# # my_func('ankit')
# class A:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     # def get_name(self):
#     #     return self.__name,self.__age
#     def salary():
#         return 100000
#     # def __repr__(self) -> str:
#     #     return self.__name,self.__age
# class B(A):
#     # pass
#     def __init__(self,name1,age1,salary):
#         super().__init__(name1,age1)
#         self.salary = salary
#     def salary():
#         super().salary()
#     # super().__init__
#     # def get_name(self):
#     #     return self.__name,self.__age
#     def salary():
#         pass
# a = A('ankit',28)
# b = B('sambhu',27,5000000)
# b.salary()
# print(b.get_name())
# print(help(B))
# print(a.get_name())

# list1 = [1,2]
# string = 'ankit'
# print(isinstance(string,str))

# cimport concurrent.futures

# [rest of code]
import concurrent.futures
import logging
import time
import threading
def thread_function():
    print('hello')
    time.sleep(2)
    print('done')
thread_list = []
# if __name__ == '__main__':
#     for i in range(10):
#         t = threading.Thread(target=thread_function,args=())
#         thread_list.append(t)
#         t.start()
#     for thread in thread_list:
#         thread.join()
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function,range(10))