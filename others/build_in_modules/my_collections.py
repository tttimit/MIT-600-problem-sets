from collections import defaultdict
from collections import namedtuple
from collections import deque
from collections import OrderedDict
from collections import Counter

# namedtuple
# a subclass of tuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(2, 3)
print("p.x=", p.x)
print("p.y=", p.y)

# dequeue
# support append() appendleft() pop() popleft()
# very efficient
d = deque(['a', 'b', 'c'])
d.append('d')
d.appendleft('1')
d.pop()
d.popleft()

# defaultdict
# return a function if the key not exists
d = defaultdict(lambda: 'N/A')
print("defaultdict: d[\'a\']=", d['a'])

# OrderedDict
# always return items as the order they inserted
od = OrderedDict([('a', 1), ('c', 3), ('b', 2)])
print(od)

# Counter
# a subclass of dict
c = Counter()
for ch in 'programming':
    c[ch] += 1

print("Counter:", c)
