from tensorflow import (Session, add, constant, int16,
                        matmul, multiply, placeholder)

# declaring constants a & b
a = constant(2)
b = constant(3)

# printing a & b values
print("a =", Session().run(a))
print("b =", Session().run(b))

print("as constants :")
print("a + b =", Session().run(a + b))
print("a * b =", Session().run(a * b))

# declaring placeholders for int-16
var1 = placeholder(int16)
var2 = placeholder(int16)

# declaring functions with previously created int-16 placeholders as parameters
randFun1 = add(var1, var2)
randFun2 = multiply(var1, var2)

# passing numbers to functions and printing output
print("as variables :")
print("a + b :", Session().run(randFun1, feed_dict={var1: 2, var2: 3}))
print("a * b :", Session().run(randFun2, feed_dict={var1: 2, var2: 3}))

# creating matrices matrix1 & matrix2
matrix1 = constant([[3., 3.]])
matrix2 = constant([[2.], [2.]])

# printing matrices multiplication
print("matrix multiplication :")
print("matrix 1 :", Session().run(matrix1))
print("matrix 2 :", Session().run(matrix2))
print("product :")
print(Session().run(matmul(matrix1, matrix2)))
