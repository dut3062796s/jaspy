class ContextManager:
    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        return False

try:
    with ContextManager() as context_manager:
        print(context_manager)
        raise RuntimeError('test context manager')
except RuntimeError:
    print('exception has not been caught')


def test1():
    with ContextManager() as context_manager:
        print(context_manager)
        return 123

print(test1())


def test():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6

print(*test())

import sys

print(sys.jaspy_version_info)
print(sys.copyright)
print(sys.version_info)
print(sys.version_info.major)

print(sys.argv)

sys.argv.append(123)
print(sys.argv)

a = 5
print(a)


def abc():
    print('abc')


abc()

def try_test1():
    try:
        try:
            return 4
        finally:
            print('finally')
            raise TypeError()
    except TypeError:
        print('except')
        pass
    print('return')
    return 5

assert try_test1() == 5




import dom
import time
import sys

import example

print(example)
example.example()

print('Implementation:', sys.implementation)

print(__name__)
print(dom)
print(time)

wrapper = dom.Element()
print('wrapper', wrapper)
print('css', wrapper.css)
wrapper.css('background', '#FF0000')
print(wrapper.css('background'))


def on_click(element):
    print('click on element', element)


p1 = wrapper.p
p1.text = 'Hallo Welt!'
p1.register_listener('click', on_click)
print(p1)
print(p1.text)

print('cls')

class Test:
    pass

print(Test)

p = wrapper.p
p['style'] = 'background: #00FF00'
p.html = '<strong>Hallo Python!</strong>'

print(Test.__str__)
print(Test.__name__)

Test.__name__ = 'Test2'

try:
    Test.__name__ = p1
except TypeError:
    print(Test)

print(Test.__class__)

try:
    Test.__class__ = int
except TypeError:
    print('yes')


class Test2():
    pass

x = Test()
x.__class__ = Test2

print(x)

print(int('ff', 16))





def hello(name='World'):
    print('Hello,', name + '!')


hello()

x = 3
print(-x)

print(dom.get_body())

dom.get_body().append(wrapper)

a = dom.Element('a')
a['href'] = '#'
a.text = 'ABC'

p.append(a)

print(x < 10)

print(x + 10)

x += 10

print(x)

#print(time.time())

start = time.time()
x = 0
while x < 5000: x += 1
stop = time.time()
print(x)
print(stop - start)

print(str(dom))

print('abc'.startswith('a'))


class ABC:
    def __init__(self):
        raise TypeError()


print(ABC is ABC)

try:
    ABC()
except TypeError:
    pass



def abc():
    int(None)


try:
    abc()
except TypeError:
    pass


def recursion(value):
    if value <= 0:
        raise Exception('check propagation')
    recursion(value - 1)

try:
    recursion(10)
except Exception:
    pass

def outer():
    x = 0;
    def inner(b: int, c: '123'=None) -> True:
        print(x)
    return inner

print(outer())


print(sys.__name__)


def on_interval(handle):
    print('Hello!!!')

dom.set_interval(5000, on_interval)


import greenlet


def sub_switch():
    greenlet.getcurrent().parent.switch()


def green_simple():
    print('simple 1')
    sub_switch()
    print('simple 2')
    sub_switch()
    print('simple 3')


def green_switch():
    print('green enter')
    green.switch()
    print('green leave')


print('main', greenlet.getcurrent())
green = greenlet.greenlet(green_simple)
print('simple', green)
print('main 1')
green.switch()
print('main 2')
green.switch()
print('main 3')
green_switch()
print('main 4')


class Test:
    def __init__(self):
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < 10:
            self.counter += 1
            return self.counter
        raise StopIteration()

for i in Test():
    print(i)

print([i for i in Test()])


def countdown():
    print('countdown started')
    counter = 10
    while counter >= 0:
        yield counter
        print('continue countdown')
        counter -= 1
    return 'abc'

g = countdown()
print(g.__next__())
print(g.__next__())
print(g.__next__())

for i in countdown():
    print(i)

print([i for i in countdown()])

from example import example as ex

print(ex)
print(ex())

print(example)

from example import *

print(example)
example()

class Test:
    def __getitem__(self, name):
        print(name)

Test()[1:3]


try:
    from ..test import test
except ImportError:
    print('no relative imports')


a = '\N{MAHJONG TILE GREEN DRAGON}'
print(a)
print(len(a))

x = True
height = 0
while True:
    time.sleep(0.02)
    height += 1
    p.css('height', str(height) + 'px')
    height %= 100
    if height == 0:
        if x:
            p.css('background', '#00FF00')
            x = False
        else:
            p.css('background', '#0000FF')
            x = True
