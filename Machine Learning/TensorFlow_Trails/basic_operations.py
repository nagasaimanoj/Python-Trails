from tensorflow import (Session, add, constant, matmul, multiply, placeholder)

if __name__ == "__main__":
    a = constant(2)
    b = constant(3)

    print("a =", Session().run(a))
    print("b =", Session().run(b))

    print("as constants :")
    print("a + b =", Session().run(a + b))
    print("a * b =", Session().run(a * b))

    var1 = placeholder(int16)
    var2 = placeholder(int16)

    randFun1 = add(var1, var2)
    randFun2 = multiply(var1, var2)

    print("as variables :")
    print("a + b :", Session().run(randFun1, feed_dict={var1: 2, var2: 3}))
    print("a * b :", Session().run(randFun2, feed_dict={var1: 2, var2: 3}))

    matrix1 = constant([[3., 3.], [1., 1.]])
    matrix2 = constant([[1., 0.], [0., 1.]])

    print("matrix multiplication :")
    print("matrix 1 :", Session().run(matrix1))
    print("matrix 2 :", Session().run(matrix2))
    print("product :")
    print(Session().run(matmul(matrix1, matrix2)))
