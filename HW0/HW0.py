import util

"""
Note: the TF's grading script may include additional test cases beyond those
given below, so you should extend this on your own to test your code.
"""

"""
Problem 1

Write a function called `matrix_multiply` which multiplies two 2-dimensional
lists of real numbers. For instance,
"""

mm = util.matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
# should evaluate to
assert(mm == [[19, 22], [43, 50]])

a = [[1,8],[3,9]]
b = [[5,10],[3,8]]
c = [[1,2,3],[4,5,6]]

m1 = util.matrix_multiply(a,b)
m2 = util.matrix_multiply(b,a)
m3 = util.matrix_multiply(a,c)
m4 = util.matrix_multiply(b,c)

assert(m1 == [[29, 74], [42, 102]])
assert(m2 == [[35, 130], [27, 96]])
assert(m3 == [[33, 42, 51], [39, 51, 63]])
assert(m4 == [[45, 60, 75], [35, 46, 57]])



"""
Problem 2

Complete the definitions of the methods `init`, `push` and `pop` in the Python
classes `MyQueue` and `MyStack`, using a deque data structure in Python.
The operation pop should return, not print, the appropriate object in the
structure. If empty, it should return None instead of throwing an error.
On the other hand, operation push does not have to return anything.

An example behavior is as follows:
"""

s = util.MyStack()

assert(s.pop() == None)

s.push(1)
s.push(2)
s.push(3)
# should evaluate to
assert(s.pop() == 3)

q = util.MyQueue()

assert(q.pop() == None)
q.push(1)
q.push(2)
q.push(3)
# should evaluate to
assert(q.pop() == 1)

"""
Problem 3
For the two classes written in Problem 2, override __eq__, __ne__, and __str__
methods. You can read about these methods in detail here:

http://docs.python.org/reference/datamodel.html#basic-customization

Simply put, the above methods do the following:

* __eq__(self, other) returns True if self and other are `equal`.

* __ne__(self, other) returns True if self and other are `not equal`.

* __str__(self) returns a string representation of self. You may decide on
whatever representation you want, but ideally the method should at least
print the elements.

We will call two stacks or two queues _equal_ if and only if they contain the
same elements and in the same order. You may assume that only elements they
contain are integers.

"""
q2 = util.MyQueue()
q2.push(3)
q2.push(2)
q2.push(1)

s2 = util.MyQueue()
s2.push(3)
s2.push(2)
s2.push(1)

assert(q.__eq__(q) == True)
assert(q.__ne__(q) == False)
assert(q.__eq__(q2) == False)
assert(q.__ne__(q2) == True)
assert(s.__eq__(s) == True)
assert(s.__ne__(s) == False)
assert(s.__eq__(s2) == False)
assert(s.__ne__(s2) == True)

"""
Problem 4

Write three functions called `add_position_iter`, `add_position_recur`, and
`add_position_map`, using iteration, recursion, and the built-in map function,
respectively. All the versions should take a list of numbers and return a new
list containing, in order, each of the original numbers incremented by the
position of that number in the list. Positions in lists are numbered starting
with 0, so:
"""

ret = util.add_position_iter([7, 5, 1, 4])
assert(ret == [7, 6, 3, 7])
# Remember that this function should not be destructive i.e.,
a = [7, 5, 1, 4]
ret = util.add_position_iter(a)
assert(a != [7, 6, 3, 7])

"""
Furthermore, your function should also take an optional argument number_from
which, although its default value should be 0, can be used to specify a
different value from which to start numbering positions, such that instead
of incrementing the first element by 0, the second by 1, etc., the function
will increment the first element by the value of number_from, the second
element by number_from+1,etc. For example:
"""

ret = util.add_position_iter([0, 0, 3, 1], number_from=3)
assert(ret == [3, 4, 8, 7])

"""
Problem 5

Write a function called `remove_course` which takes in `roster`, `student`,
`course` as arguments and returns a modified roster. This function,
unlike ones you've just written, should be destructive, meaning that
roster should be modified directly.

* `roster` will be of type dictionary in Python. It will map a string (i.e., a
student name) to a set. Each set will contain strings, representing courses the
corresponding student is currently taking.
* `student` will be of type string; it will represent the name of the student.
* `course` will also be of type string.

You can read more about set and dict below:

http://docs.python.org/tutorial/datastructures.html#sets
http://docs.python.org/tutorial/datastructures.html#dictionaries

An example behavior is as follows:
"""

roster = {'kyu': set(['cs182']), 'david': set(['cs182'])}
util.remove_course(roster, 'kyu', 'cs182')
assert(roster == {'kyu': set([]), 'david': set(['cs182'])})

"""
Problem 6

Now write a function called `copy_remove_course`. The specifications are the
same as above except the function should now be non-destructive.
An example behavior is as follows:
"""

roster = {'kyu': set(['cs182']), 'david': set(['cs182'])}
new_roster = util.copy_remove_course(roster, 'kyu', 'cs182')
assert(roster == {'kyu': set(['cs182']), 'david': set(['cs182'])})
assert(new_roster == {'kyu': set([]), 'david': set(['cs182'])})

"""
Hint: _copy_ the original roster and apply remove_course from Problem 5.

You can read more about the copy module below:
http://docs.python.org/2/library/copy.html
"""
