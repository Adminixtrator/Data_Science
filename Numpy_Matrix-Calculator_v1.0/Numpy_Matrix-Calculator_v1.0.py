import numpy as admin

print('''\n\t -------------------\n\t| MATRIX CALCULATOR |
\t -------------------\n\n''')

while True:
    print('''[1.] Determinant\n[2.] Transpose\n[3.] Inverse
[4.] Addition\n[5.] Subtraction\n[6.] Multiplication\n[7.] Division\n''')
    op = input("Please select operation e.g 1\n")
#-------- CONDITIONS ----------
    #A1--------
#----------------------------| OPERATION 01 |------------------------------------------------------------------

    if op == '1':
        asd = input("Please enter the dimension of the matrix e.g 4,4\n")
        #Aa1----------
        if asd == '3,3':
            a11 = int(input('''Please enter a11 a12 a13 a21 to a33 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a21 = int(input())
            a22 = int(input())
            a23 = int(input())
            a31 = int(input())
            a32 = int(input())
            a33 = int(input())
            #HANDLER---------
            matA = admin.arange(1,10).reshape(3,3)
            matA.flat[[0,1,2,3,4,5,6,7,8]] = a11,a12,a13,a21,a22,a23,a31,a32,a33
            det = (a11*((a22*a33)-(a23*a32))) - (a12*((a21*a33)-(a23*a31))) + (a13*((a21*a32)-(a22*a31)))
            #Output----------
            print('MATRIX:\n',matA)
            print('\nDeterminant: ',det,'\n\n')
        #Aa2----------
        elif asd == '2,2':
            a11 = int(input('''Please enter a11 a12 a21 a22 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a21 = int(input())
            a22 = int(input())
            #HANDLER---------
            matA = admin.arange(1,5).reshape(2,2)
            matA.flat[[0,1,2,3]] = a11,a12,a21,a22
            det = ((a11*a22) - (a12*a21))
            #Output----------
            print('MATRIX:\n',matA)
            print('\nDeterminant: ',det,'\n\n')
        #Aa3-----------
        elif asd == '4,4':
            a11 = int(input('''Please enter a11 a12 a13 a14 to a44 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a14 = int(input())
            a21 = int(input())
            a22 = int(input())
            a23 = int(input())
            a24 = int(input())
            a31 = int(input())
            a32 = int(input())
            a33 = int(input())
            a34 = int(input())
            a41 = int(input())
            a42 = int(input())
            a43 = int(input())
            a44 = int(input())
            #HANDLER---------
            matA = admin.arange(1,17).reshape(4,4)
            matA.flat[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]] = a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34
            det = (a11*a22*a33*a44)-(a12*a23*a34*a41)+(a13*a24*a31*a42)-(a14*a21*a32*43)+(a14*a23*a32*a41)-(a11*a24*a33*42)+(a12*a21*a34*a43)-(a13*a22*a31*a44)
            #Output----------
            print('MATRIX:\n',matA)
            print('\nDeterminant: ',det,'\n\n')
        #Aa4-----------
        else:
            print('''Dimension error--
 --Operation cannot be performed with given matrix.\n''')
#---------------------------------------------------------------------------------------------------------------
    #A2--------
#----------------------------| OPERATION 02 |------------------------------------------------------------------

    elif op == '2':
        asd = input("Please enter the dimension of the matrix e.g 2,3\n")
        #B1--------
        if asd == '2,2':
            a11 = int(input('''Please enter a11 a12 a21 a22 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a21 = int(input())
            a22 = int(input())
            #HANDLER---------
            matA = admin.arange(1,5).reshape(2,2)
            matA.flat[[0,1,2,3]] = a11,a12,a21,a22
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA)
            print('\nTranspose: \n',trans,'\n\n')
        #B2---------
        elif asd == '2,3':
            a11 = int(input('''Please enter a11 a12 a13 a21 a22 a23 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a21 = int(input())
            a22 = int(input())
            a23 = int(input())
            #HANDLER---------
            matA = admin.arange(1,7).reshape(2,3)
            matA.flat[[0,1,2,3,4,5]] = a11,a12,a13,a21,a22,a23
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA)
            print('\nTranspose: \n',trans,'\n\n')
        #B3---------
        elif asd == '3,2':
            a11 = int(input('''Please enter a11 a12 a21 a22 a31 a32 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a21 = int(input())
            a22 = int(input())
            a31 = int(input())
            a32 = int(input())
            #HANDLER---------
            matA = admin.arange(1,7).reshape(3,2)
            matA.flat[[0,1,2,3,4,5]] = a11,a12,a21,a22,a31,a32
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA)
            print('\nTranspose: \n',trans,'\n\n')
        #B4---------
        elif asd == '3,3':
            a11 = int(input('''Please enter a11 a12 a13 a21 to a33 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a21 = int(input())
            a22 = int(input())
            a23 = int(input())
            a31 = int(input())
            a32 = int(input())
            a33 = int(input())
            #HANDLER---------
            matA = admin.arange(1,10).reshape(3,3)
            matA.flat[[0,1,2,3,4,5,6,7,8]] = a11,a12,a13,a21,a22,a23,a31,a32,a33
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA)
            print('\nTranspose: \n',trans,'\n\n')
        #B5----------
        elif asd == '2,1':
            a11 = int(input('''Please enter a11 and a21 respectively--
 --Pressing enter after each input.\n'''))
            a21 = int(input())
            #HANDLER---------
            matA = admin.arange(1,3).reshape(2,1)
            matA.flat[[0,1]] = a11,a21
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA)
            print('\nTranspose: \n',trans,'\n\n')
        #B6---------
        elif asd == '3,1':
            a11 = int(input('''Please enter a11 a21 and a31 respectively--
 --Pressing enter after each input.\n'''))
            a21 = int(input())
            a31 = int(input())
            #HANDLER---------
            matA = admin.arange(1,4).reshape(3,1)
            matA.flat[[0,1,2]] = a11,a21,a31
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA)
            print('\nTranspose: \n',trans,'\n\n')
        #B7---------
        elif asd == '1,2':
            a11 = int(input('''Please enter a11 and a12 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            #HANDLER---------
            matA = admin.arange(1,3).reshape(1,2)
            matA.flat[[0,1]] = a11,a12
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA)
            print('\nTranspose: \n',trans,'\n\n')

        #B8---------
        elif asd == '1,3':
            a11 = int(input('''Please enter a11 a12 and a13 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            #HANDLER---------
            matA = admin.arange(1,4).reshape(1,3)
            matA.flat[[0,1,2]] = a11,a12,a13
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA)
            print('\nTranspose: \n',trans,'\n\n')
        #B9---------
        elif asd == '1,4':
            a11 = int(input('''Please enter a11 a12 a13 and a14 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a14 = int(input())
            #HANDLER---------
            matA = admin.arange(1,5).reshape(1,4)
            matA.flat[[0,1,2,3]] = a11,a12,a13,a14
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA)
            print('\nTranspose: \n',trans,'\n\n')
        #B10---------
        elif asd == '4,1':
            a11 = int(input('''Please enter a11 a21 a31 and a41 respectively--
 --Pressing enter after each input.\n'''))
            a21 = int(input())
            a31 = int(input())
            a41 = int(input())
            #HANDLER---------
            matA = admin.arange(1,5).reshape(4,1)
            matA.flat[[0,1,2,3]] = a11,a21,a31,a41
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA)
            print('\nTranspose: \n',trans,'\n\n')
            #B11---------
        elif asd == '4,3':
            a11 = int(input('''Please enter a11 a12 a13 a21 to a43 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a21 = int(input())
            a22 = int(input())
            a23 = int(input())
            a31 = int(input())
            a32 = int(input())
            a33 = int(input())
            a41 = int(input())
            a42 = int(input())
            a43 = int(input())
            #HANDLER---------
            matA = admin.arange(1,13).reshape(4,3)
            matA.flat[[0,1,2,3,4,5,6,7,8,9,10,11]] = a11,a12,a13,a21,a22,a23,a31,a32,a33,a41,a42,a43
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA)
            print('\nTranspose: \n',trans,'\n\n')
        #B12---------
        elif asd == '3,4':
            a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a34 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a14 = int(input())
            a21 = int(input())
            a22 = int(input())
            a23 = int(input())
            a24 = int(input())
            a31 = int(input())
            a32 = int(input())
            a33 = int(input())
            a34 = int(input())
            #HANDLER---------
            matA = admin.arange(1,13).reshape(3,4)
            matA.flat[[0,1,2,3,4,5,6,7,8,9,10,11]] = a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA)
            print('\nTranspose: \n',trans,'\n\n')
        #B13---------
        elif asd == '4,2':
            a11 = int(input('''Please enter a11 a12 a21 to a42 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a21 = int(input())
            a22 = int(input())
            a31 = int(input())
            a32 = int(input())
            a41 = int(input())
            a42 = int(input())
            #HANDLER---------
            matA = admin.arange(1,9).reshape(4,2)
            matA.flat[[0,1,2,3,4,5,6,7]] = a11,a12,a21,a22,a31,a32,a41,a42
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA)
            print('\nTranspose: \n',trans,'\n\n')
        #B14---------
        elif asd == '2,4':
            a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a24 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a14 = int(input())
            a21 = int(input())
            a22 = int(input())
            a23 = int(input())
            a24 = int(input())
            #HANDLER---------
            matA = admin.arange(1,9).reshape(2,4)
            matA.flat[[0,1,2,3,4,5,6,7]] = a11,a12,a13,a14,a21,a22,a23,a24
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA)
            print('\nTranspose: \n',trans,'\n\n')
        #B15---------
        elif asd == '4,4':
            a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a44 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a14 = int(input())
            a21 = int(input())
            a22 = int(input())
            a23 = int(input())
            a24 = int(input())
            a31 = int(input())
            a32 = int(input())
            a33 = int(input())
            a34 = int(input())
            a41 = int(input())
            a42 = int(input())
            a43 = int(input())
            a44 = int(input())
            #HANDLER---------
            matA = admin.arange(1,17).reshape(4,4)
            matA.flat[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]] = a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34,a41,a42,a43,a44
            trans = admin.transpose(matA)
            #Output----------
            print('MATRIX:\n',matA)
            print('\nTranspose: \n',trans,'\n\n')
        #B16----------
        else:
            print('''\nInvalid matrix dimension--
 --Please check your input and try again!\n\n''')
#--------------------------------------------------------------------------------------------------------------
    #A3--------
#----------------------------| OPERATION 03 |------------------------------------------------------------------

    elif op == '3':
        asd = input("Please enter the dimension of the matrix e.g 3,3\n")
        #C1----------
        if asd == '3,3':
            a11 = int(input('''Please enter a11 a12 a13 a21 to a33 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a21 = int(input())
            a22 = int(input())
            a23 = int(input())
            a31 = int(input())
            a32 = int(input())
            a33 = int(input())
            #HANDLER---------
            matA = admin.arange(1,10).reshape(3,3)
            matA.flat[[0,1,2,3,4,5,6,7,8]] = a11,a12,a13,a21,a22,a23,a31,a32,a33
            det = (a11*((a22*a33)-(a23*a32))) - (a12*((a21*a33)-(a23*a31))) + (a13*((a21*a32)-(a22*a31)))           
            #Output----------
            if det == 0:
                print("\nDeterminant = 0\n --Please enter a valid matrix.\n\n")
            else:
                print('MATRIX:\n',matA)          
                a11 = (a11/det)
                a12 = (a12/det)
                a13 = (a13/det)
                a21 = (a21/det)
                a22 = (a22/det)
                a23 = (a23/det)
                a31 = (a31/det)
                a32 = (a32/det)
                a33 = (a33/det)
                inv = matA.flat[[0,1,2,3,4,5,6,7,8]] = a11,a12,a13,a21,a22,a23,a31,a32,a33
                inv = admin.transpose(inv)
                print('\nINVERSE:\n',inv.reshape(3,3),'\n')
                print('\nDeterminant: ',det,'\n\n')
        #C2----------
        elif asd == '2,2':
            a11 = int(input('''Please enter a11 a12 a21 a22 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a21 = int(input())
            a22 = int(input())
            #HANDLER---------
            matA = admin.arange(1,5).reshape(2,2)
            matA.flat[[0,1,2,3]] = a11,a12,a21,a22
            det = ((a11*a22) - (a12*a21))
            #Output----------
            if det == 0:
                print("\nDeterminant = 0\n --Please enter a valid matrix.\n\n")
            else:
                print('MATRIX:\n',matA)          
                a11 = (a11/det)
                a12 = (a12/det)
                a21 = (a21/det)
                a22 = (a22/det)
                inv = matA.flat[[0,1,2,3]] = a11,a12,a21,a22
                inv = admin.transpose(inv)
                print('\nINVERSE:\n',inv.reshape(2,2),'\n')
                print('\nDeterminant: ',det,'\n\n')
        #C3-----------
        elif asd == '4,4':
            a11 = int(input('''Please enter a11 a12 a13 a14 to a44 respectively--
 --Pressing enter after each input.\n'''))
            a12 = int(input())
            a13 = int(input())
            a14 = int(input())
            a21 = int(input())
            a22 = int(input())
            a23 = int(input())
            a24 = int(input())
            a31 = int(input())
            a32 = int(input())
            a33 = int(input())
            a34 = int(input())
            a41 = int(input())
            a42 = int(input())
            a43 = int(input())
            a44 = int(input())
            #HANDLER---------
            matA = admin.arange(1,17).reshape(4,4)
            matA.flat[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]] = a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34
            det = (a11*((a22*a33)-(a23*a32))) - (a12*((a21*a33)-(a23*a31))) + (a13*((a21*a32)-(a22*a31)))
            #Output----------
            if det == 0:
                print("\nDeterminant = 0\n --Please enter a valid matrix.\n\n")
            else:
                print('MATRIX:\n',matA)          
                a11 = (a11/det)
                a12 = (a12/det)
                a13 = (a13/det)
                a14 = (a14/det)
                a21 = (a21/det)
                a22 = (a22/det)
                a23 = (a23/det)
                a24 = (a24/det)
                a31 = (a31/det)
                a32 = (a32/det)
                a33 = (a33/det)
                a34 = (a34/det)
                a41 = (a41/det)
                a42 = (a42/det)
                a43 = (a43/det)
                a44 = (a44/det)
                matA.flat[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]] = a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34
                inv = admin.transpose(inv)
                print('\nINVERSE:\n',inv.reshape(4,4),'\n')
                print('\nDeterminant: ',det,'\n\n')
        #C4-----------
        else:
            print('''Dimension error--
 --Operation cannot be performed with given matrix.\n''')
#--------------------------------------------------------------------------------------------------------------
    #A4--------
#----------------------------| OPERATION 04 |------------------------------------------------------------------
    elif op == '4':
        asd = input("Please enter the dimension of the matA e.g 3,2\n")
        #------ CHECK --------
        if asd == '2,2' or asd == '3,3' or asd == '4,4' or asd == '2,1' or asd == '1,2' or asd == '1,3' or asd == '1,4' or asd == '2,3' or asd == '2,4' or asd == '4,2' or asd == '3,2' or asd == '3,4' or asd == '3,1' or asd == '4,1' or asd == '4,2' or asd == '4,3' :
            asc = input("Please enter the dimension of the matB e.g 3,2\n")
            #D1--------
            if asc == '2,2':
                a11 = int(input('''Please enter a11 a12 a21 a22 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a21 = int(input())
                a22 = int(input())
                b11 = int(input('''Please enter b11 b12 b21 b22 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b21 = int(input())
                b22 = int(input())
                #HANDLER---------
                matA = admin.arange(1,5).reshape(2,2)
                matA.flat[[0,1,2,3]] = a11,a12,a21,a22
                matB = admin.arange(1,5).reshape(2,2)
                matB.flat[[0,1,2,3]] = b11,b12,b21,b22
                matC = admin.arange(1,5).reshape(2,2)
                matC.flat[[0,1,2,3]] = a11+b11,a12+b12,a21+b21,a22+b22
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nAddition: \n',matC,'\n\n')
            #D2---------
            elif asc == '2,3':
                a11 = int(input('''Please enter a11 a12 a13 a21 a22 a23 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b21 b22 b23 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                #HANDLER---------
                matA = admin.arange(1,7).reshape(2,3)
                matA.flat[[0,1,2,3,4,5]] = a11,a12,a13,a21,a22,a23
                matB = admin.arange(1,7).reshape(2,3)
                matB.flat[[0,1,2,3,4,5]] = b11,b12,b13,b21,b22,b23
                matA = admin.arange(1,7).reshape(2,3)
                matA.flat[[0,1,2,3,4,5]] = a11+b11,a12+b12,a13+b13,a21+b21,a22+b22,a23+b23
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nAddition: \n',matC,'\n\n')
            #D3---------
            elif asc == '3,2':
                a11 = int(input('''Please enter a11 a12 a21 a22 a31 a32 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a21 = int(input())
                a22 = int(input())
                a31 = int(input())
                a32 = int(input())
                b11 = int(input('''Please enter b11 b12 b21 b22 b31 b32 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b21 = int(input())
                b22 = int(input())
                b31 = int(input())
                b32 = int(input())
                #HANDLER---------
                matA = admin.arange(1,7).reshape(3,2)
                matA.flat[[0,1,2,3,4,5]] = a11,a12,a21,a22,a32,a32
                matB = admin.arange(1,7).reshape(3,2)
                matB.flat[[0,1,2,3,4,5]] = b11,b12,b21,b22,b32,b32
                matC = admin.arange(1,7).reshape(3,2)
                matC.flat[[0,1,2,3,4,5]] = a11+b11,a12+b12,a21+b21,a22+b22,a31+b31,a32+b32
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nAddition: \n',matC,'\n\n')
            #D4---------
            elif asc == '3,3':
                a11 = int(input('''Please enter a11 a12 a13 a21 to a33 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b21 to b33 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b31 = int(input())
                b32 = int(input())
                b33 = int(input())
                #HANDLER---------
                matA = admin.arange(1,10).reshape(3,3)
                matA.flat[[0,1,2,3,4,5,6,7,8]] = a11,a12,a13,a21,a22,a23,a31,a32,a33
                matB = admin.arange(1,10).reshape(3,3)
                matB.flat[[0,1,2,3,4,5,6,7,8]] = b11,b12,b13,b21,b22,b23,b31,b32,b33
                matC = admin.arange(1,10).reshape(3,3)
                matC.flat[[0,1,2,3,4,5,6,7,8]] = a11+b11,a12+b12,a13+b13,a21+b21,a22+b22,a23+b23,a31+b31,a32+b32,a33+b33
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nAddition: \n',matC,'\n\n')
            #D5----------
            elif asc == '2,1':
                a11 = int(input('''Please enter a11 and a21 of matA respectively--
 --Pressing enter after each input.\n'''))
                a21 = int(input())
                b11 = int(input('''Please enter b11 and b21 of matB respectively--
 --Pressing enter after each input.\n'''))
                b21 = int(input())
                #HANDLER---------
                matA = admin.arange(1,3).reshape(2,1)
                matA.flat[[0,1]] = a11,a21
                matB = admin.arange(1,3).reshape(2,1)
                matB.flat[[0,1]] = b11,b21
                matC = admin.arange(1,3).reshape(2,1)
                matC.flat[[0,1]] = a11+b11,a21+b21
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nAddition: \n',matC,'\n\n')
            #D6---------
            elif asc == '3,1':
                a11 = int(input('''Please enter a11 a21 and a31 of matA respectively--
 --Pressing enter after each input.\n'''))
                a21 = int(input())
                a31 = int(input())
                b11 = int(input('''Please enter b11 b21 and b31 of matB respectively--
 --Pressing enter after each input.\n'''))
                b21 = int(input())
                b31 = int(input())
                #HANDLER---------
                matA = admin.arange(1,4).reshape(3,1)
                matA.flat[[0,1,2]] = a11,a21,a31
                matB = admin.arange(1,4).reshape(3,1)
                matB.flat[[0,1,2]] = b11,b21,b31
                matC = admin.arange(1,4).reshape(3,1)
                matC.flat[[0,1,2]] = a11+b11,a21+b21,a31+b31
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nAddition: \n',matC,'\n\n')
            #D7---------
            elif asc == '1,2':
                a11 = int(input('''Please enter a11 and a12 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                b11 = int(input('''Please enter b11 and b12 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                #HANDLER---------
                matA = admin.arange(1,3).reshape(1,2)
                matA.flat[[0,1]] = a11,a12
                matB = admin.arange(1,3).reshape(1,2)
                matB.flat[[0,1]] = b11,b12
                matC = admin.arange(1,3).reshape(1,2)
                matC.flat[[0,1]] = a11+b11,a12+b12
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nAddition: \n',matC,'\n\n')
            #D8---------
            elif asc == '1,3':
                a11 = int(input('''Please enter a11 a12 and a13 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                b11 = int(input('''Please enter b11 b12 and b13 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                #HANDLER---------
                matA = admin.arange(1,4).reshape(1,3)
                matA.flat[[0,1,2]] = a11,a12,a13
                matB = admin.arange(1,4).reshape(1,3)
                matB.flat[[0,1,2]] = b11,b12,b13
                matC = admin.arange(1,4).reshape(1,3)
                matC.flat[[0,1,2]] = a11+b11,a12+a12,a13+a13
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nAddition: \n',matC,'\n\n')
            #D9---------
            elif asc == '1,4':
                a11 = int(input('''Please enter a11 a12 a13 and a14 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 and a14 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b14 = int(input())
                #HANDLER---------
                matA = admin.arange(1,5).reshape(1,4)
                matA.flat[[0,1,2,3]] = a11,a12,a13,a14
                matB = admin.arange(1,5).reshape(1,4)
                matB.flat[[0,1,2,3]] = b11,b12,b13,b14
                matC = admin.arange(1,5).reshape(1,4)
                matC.flat[[0,1,2,3]] = a11+b11,a12+b12,a13+b13,a14+b14
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nAddition: \n',matC,'\n\n')
            #D10---------
            elif asc == '4,1':
                a11 = int(input('''Please enter a11 a21 a31 and a41 of matA respectively--
 --Pressing enter after each input.\n'''))
                a21 = int(input())
                a31 = int(input())
                a41 = int(input())
                b11 = int(input('''Please enter b11 b21 b31 and b41 of matB respectively--
 --Pressing enter after each input.\n'''))
                b21 = int(input())
                b31 = int(input())
                b41 = int(input())
                #HANDLER---------
                matA = admin.arange(1,5).reshape(4,1)
                matA.flat[[0,1,2,3]] = a11,a21,a31,a41
                matB = admin.arange(1,5).reshape(4,1)
                matB.flat[[0,1,2,3]] = b11,b21,b31,b41
                matC = admin.arange(1,5).reshape(4,1)
                matC.flat[[0,1,2,3]] = a11+b11,a21+b21,a31+b31,a41+b41
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nAddition: \n',matC,'\n\n')
            #D11---------
            elif asc == '4,3':
                a11 = int(input('''Please enter a11 a12 a13 a21 to a43 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                a41 = int(input())
                a42 = int(input())
                a43 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b21 to b43 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b31 = int(input())
                b32 = int(input())
                b33 = int(input())
                b41 = int(input())
                b42 = int(input())
                b43 = int(input())
                #HANDLER---------
                matA = admin.arange(1,13).reshape(4,3)
                matA.flat[[0,1,2,3,4,5,6,7,8,9,10,11]] = a11,a12,a13,a21,a22,a23,a31,a32,a33,a41,a42,a43
                matB = admin.arange(1,13).reshape(4,3)
                matB.flat[[0,1,2,3,4,5,6,7,8,9,10,11]] = b11,b12,b13,b21,b22,b23,b31,b32,b33,b41,b42,b43
                matC = admin.arange(1,13).reshape(4,3)
                matC.flat[[0,1,2,3,4,5,6,7,8,9,10,11]] = a11+b11,a12+b12,a13+b13,a21+b21,a22+b22,a23+b23,a31+b31,a32+b32,a33+b33,a41+b41,a42+b42,a43+b43
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nAddition: \n',matC,'\n\n')
            #D12---------
            elif asc == '3,4':
                a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a34 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a24 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                a34 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b14 b21 to b34 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b14 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b24 = int(input())
                b31 = int(input())
                b32 = int(input())
                b33 = int(input())
                b34 = int(input())
                #HANDLER---------
                matA = admin.arange(1,13).reshape(3,4)
                matA.flat[[0,1,2,3,4,5,6,7,8,9,10,11]] = a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34
                matB = admin.arange(1,13).reshape(3,4)
                matB.flat[[0,1,2,3,4,5,6,7,8,9,10,11]] = b11,b12,b13,b14,b21,b22,b23,b24,b31,b32,b33,b34
                matC = admin.arange(1,13).reshape(3,4)
                matC.flat[[0,1,2,3,4,5,6,7,8,9,10,11]] = a11+b11,a12+b12,a13+b13,a14+b14,a21+b21,a22+b22,a23+b23,a24+b24,a31+b31,a32+b32,a33+b33,a34+b34
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nAddition: \n',matC,'\n\n')
            #D13---------
            elif asc == '4,2':
                a11 = int(input('''Please enter a11 a12 a21 to a42 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a21 = int(input())
                a22 = int(input())
                a31 = int(input())
                a32 = int(input())
                a41 = int(input())
                a42 = int(input())
                b11 = int(input('''Please enter b11 b12 a21 to b42 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b21 = int(input())
                b22 = int(input())
                b31 = int(input())
                b32 = int(input())
                b41 = int(input())
                b42 = int(input())
                #HANDLER---------
                matA = admin.arange(1,9).reshape(4,2)
                matA.flat[[0,1,2,3,4,5,6,7]] = a11,a12,a21,a22,a31,a32,a41,a42
                matB = admin.arange(1,9).reshape(4,2)
                matB.flat[[0,1,2,3,4,5,6,7]] = b11,b12,b21,b22,b31,b32,b41,b42
                matC = admin.arange(1,9).reshape(4,2)
                matC.flat[[0,1,2,3,4,5,6,7]] = a11+b11,a12+b12,a21+b21,a22+b22,a31+b31,a32+b32,a41+b41,a42+b42
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nAddition: \n',matC,'\n\n')
            #D14---------
            elif asc == '2,4':
                a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a24 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a24 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b14 b21 to b24 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b14 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b24 = int(input())
                #HANDLER---------
                matA = admin.arange(1,9).reshape(2,4)
                matA.flat[[0,1,2,3,4,5,6,7]] = a11,a12,a13,a14,a21,a22,a23,a24
                matB = admin.arange(1,9).reshape(2,4)
                matB.flat[[0,1,2,3,4,5,6,7]] = b11,b12,b13,b14,b21,b22,b23,b24
                matC = admin.arange(1,9).reshape(2,4)
                matC.flat[[0,1,2,3,4,5,6,7]] = a11+b11,a12+b12,a13+b13,a14+b14,a21+b21,a22+b22,a23+b23,a24+b24
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nAddition: \n',matC,'\n\n')
            #D15---------
            elif asc == '4,4':
                a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a44 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a24 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                a34 = int(input())
                a41 = int(input())
                a42 = int(input())
                a43 = int(input())
                a44 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b14 b21 to b44 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b14 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b24 = int(input())
                b31 = int(input())
                b32 = int(input())
                b33 = int(input())
                b34 = int(input())
                b41 = int(input())
                b42 = int(input())
                b43 = int(input())
                b44 = int(input())
                #HANDLER---------
                matA = admin.arange(1,17).reshape(4,4)
                matA.flat[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]] = a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34,a41,a42,a43,a44
                matB = admin.arange(1,17).reshape(4,4)
                matB.flat[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]] = b11,b12,b13,b14,b21,b22,b23,b24,b31,b32,b33,b34,b41,b42,b43,b44
                matC = admin.arange(1,17).reshape(4,4)
                matC.flat[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]] = a11+b11,a12+b12,a13+b13,a14+b14,a21+b21,a22+b22,a23+b23,a24+b24,a31+b31,a32+b32,a33+b33,a34+b34,a41+b41,a42+b42,a43+b43,a44+b44
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nAddition: \n',matC,'\n\n')
            #D16----------
            else:
                print('''Dimension error--
 --Addition can only be performed with matrix of the same dimension.\n''')
        else:
            print('''Dimension error--
 --Operation cannot be performed with given matrix.\n''')     
#--------------------------------------------------------------------------------------------------------------
    #A5--------
#----------------------------| OPERATION 05 |------------------------------------------------------------------

    elif op == '5':
        asd = input("Please enter the dimension of the matA e.g 3,2\n")
        #------ CHECK --------
        if asd == '2,2' or asd == '3,3' or asd == '4,4' or asd == '2,1' or asd == '1,2' or asd == '1,3' or asd == '1,4' or asd == '2,3' or asd == '2,4' or asd == '4,2' or asd == '3,2' or asd == '3,4' or asd == '3,1' or asd == '4,1' or asd == '4,2' or asd == '4,3' :
            asc = input("Please enter the dimension of the matB e.g 3,2\n")
            #E1--------
            if asc == '2,2':
                a11 = int(input('''Please enter a11 a12 a21 a22 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a21 = int(input())
                a22 = int(input())
                b11 = int(input('''Please enter b11 b12 b21 b22 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b21 = int(input())
                b22 = int(input())
                #HANDLER---------
                matA = admin.arange(1,5).reshape(2,2)
                matA.flat[[0,1,2,3]] = a11,a12,a21,a22
                matB = admin.arange(1,5).reshape(2,2)
                matB.flat[[0,1,2,3]] = b11,b12,b21,b22
                matC = admin.arange(1,5).reshape(2,2)
                matC.flat[[0,1,2,3]] = a11-b11,a12-b12,a21-b21,a22-b22
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #E2---------
            elif asc == '2,3':
                a11 = int(input('''Please enter a11 a12 a13 a21 a22 a23 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b21 b22 b23 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                #HANDLER---------
                matA = admin.arange(1,7).reshape(2,3)
                matA.flat[[0,1,2,3,4,5]] = a11,a12,a13,a21,a22,a23
                matB = admin.arange(1,7).reshape(2,3)
                matB.flat[[0,1,2,3,4,5]] = b11,b12,b13,b21,b22,b23
                matA = admin.arange(1,7).reshape(2,3)
                matA.flat[[0,1,2,3,4,5]] = a11-b11,a12-b12,a13-b13,a21-b21,a22-b22,a23-b23
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #E3---------
            elif asc == '3,2':
                a11 = int(input('''Please enter a11 a12 a21 a22 a31 a32 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a21 = int(input())
                a22 = int(input())
                a31 = int(input())
                a32 = int(input())
                b11 = int(input('''Please enter b11 b12 b21 b22 b31 b32 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b21 = int(input())
                b22 = int(input())
                b31 = int(input())
                b32 = int(input())
                #HANDLER---------
                matA = admin.arange(1,7).reshape(3,2)
                matA.flat[[0,1,2,3,4,5]] = a11,a12,a21,a22,a32,a32
                matB = admin.arange(1,7).reshape(3,2)
                matB.flat[[0,1,2,3,4,5]] = b11,b12,b21,b22,b32,b32
                matC = admin.arange(1,7).reshape(3,2)
                matC.flat[[0,1,2,3,4,5]] = a11-b11,a12-b12,a21-b21,a22-b22,a31-b31,a32-b32
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #E4---------
            elif asc == '3,3':
                a11 = int(input('''Please enter a11 a12 a13 a21 to a33 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b21 to b33 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b31 = int(input())
                b32 = int(input())
                b33 = int(input())
                #HANDLER---------
                matA = admin.arange(1,10).reshape(3,3)
                matA.flat[[0,1,2,3,4,5,6,7,8]] = a11,a12,a13,a21,a22,a23,a31,a32,a33
                matB = admin.arange(1,10).reshape(3,3)
                matB.flat[[0,1,2,3,4,5,6,7,8]] = b11,b12,b13,b21,b22,b23,b31,b32,b33
                matC = admin.arange(1,10).reshape(3,3)
                matC.flat[[0,1,2,3,4,5,6,7,8]] = a11-b11,a12-b12,a13-b13,a21-b21,a22-b22,a23-b23,a31-b31,a32-b32,a33-b33
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #E5----------
            elif asc == '2,1':
                a11 = int(input('''Please enter a11 and a21 of matA respectively--
 --Pressing enter after each input.\n'''))
                a21 = int(input())
                b11 = int(input('''Please enter b11 and b21 of matB respectively--
 --Pressing enter after each input.\n'''))
                b21 = int(input())
                #HANDLER---------
                matA = admin.arange(1,3).reshape(2,1)
                matA.flat[[0,1]] = a11,a21
                matB = admin.arange(1,3).reshape(2,1)
                matB.flat[[0,1]] = b11,b21
                matC = admin.arange(1,3).reshape(2,1)
                matC.flat[[0,1]] = a11-b11,a21-b21
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #E6---------
            elif asc == '3,1':
                a11 = int(input('''Please enter a11 a21 and a31 of matA respectively--
 --Pressing enter after each input.\n'''))
                a21 = int(input())
                a31 = int(input())
                b11 = int(input('''Please enter b11 b21 and b31 of matB respectively--
 --Pressing enter after each input.\n'''))
                b21 = int(input())
                b31 = int(input())
                #HANDLER---------
                matA = admin.arange(1,4).reshape(3,1)
                matA.flat[[0,1,2]] = a11,a21,a31
                matB = admin.arange(1,4).reshape(3,1)
                matB.flat[[0,1,2]] = b11,b21,b31
                matC = admin.arange(1,4).reshape(3,1)
                matC.flat[[0,1,2]] = a11-b11,a21-b21,a31-b31
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #E7---------
            elif asc == '1,2':
                a11 = int(input('''Please enter a11 and a12 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                b11 = int(input('''Please enter b11 and b12 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                #HANDLER---------
                matA = admin.arange(1,3).reshape(1,2)
                matA.flat[[0,1]] = a11,a12
                matB = admin.arange(1,3).reshape(1,2)
                matB.flat[[0,1]] = b11,b12
                matC = admin.arange(1,3).reshape(1,2)
                matC.flat[[0,1]] = a11-b11,a12-b12
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #E8---------
            elif asc == '1,3':
                a11 = int(input('''Please enter a11 a12 and a13 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                b11 = int(input('''Please enter b11 b12 and b13 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                #HANDLER---------
                matA = admin.arange(1,4).reshape(1,3)
                matA.flat[[0,1,2]] = a11,a12,a13
                matB = admin.arange(1,4).reshape(1,3)
                matB.flat[[0,1,2]] = b11,b12,b13
                matC = admin.arange(1,4).reshape(1,3)
                matC.flat[[0,1,2]] = a11-b11,a12-a12,a13-a13
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #E9---------
            elif asc == '1,4':
                a11 = int(input('''Please enter a11 a12 a13 and a14 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 and a14 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b14 = int(input())
                #HANDLER---------
                matA = admin.arange(1,5).reshape(1,4)
                matA.flat[[0,1,2,3]] = a11,a12,a13,a14
                matB = admin.arange(1,5).reshape(1,4)
                matB.flat[[0,1,2,3]] = b11,b12,b13,b14
                matC = admin.arange(1,5).reshape(1,4)
                matC.flat[[0,1,2,3]] = a11-b11,a12-b12,a13-b13,a14-b14
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #E10---------
            elif asc == '4,1':
                a11 = int(input('''Please enter a11 a21 a31 and a41 of matA respectively--
 --Pressing enter after each input.\n'''))
                a21 = int(input())
                a31 = int(input())
                a41 = int(input())
                b11 = int(input('''Please enter b11 b21 b31 and b41 of matB respectively--
 --Pressing enter after each input.\n'''))
                b21 = int(input())
                b31 = int(input())
                b41 = int(input())
                #HANDLER---------
                matA = admin.arange(1,5).reshape(4,1)
                matA.flat[[0,1,2,3]] = a11,a21,a31,a41
                matB = admin.arange(1,5).reshape(4,1)
                matB.flat[[0,1,2,3]] = b11,b21,b31,b41
                matC = admin.arange(1,5).reshape(4,1)
                matC.flat[[0,1,2,3]] = a11-b11,a21-b21,a31-b31,a41-b41
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #E11---------
            elif asc == '4,3':
                a11 = int(input('''Please enter a11 a12 a13 a21 to a43 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                a41 = int(input())
                a42 = int(input())
                a43 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b21 to b43 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b31 = int(input())
                b32 = int(input())
                b33 = int(input())
                b41 = int(input())
                b42 = int(input())
                b43 = int(input())
                #HANDLER---------
                matA = admin.arange(1,13).reshape(4,3)
                matA.flat[[0,1,2,3,4,5,6,7,8,9,10,11]] = a11,a12,a13,a21,a22,a23,a31,a32,a33,a41,a42,a43
                matB = admin.arange(1,13).reshape(4,3)
                matB.flat[[0,1,2,3,4,5,6,7,8,9,10,11]] = b11,b12,b13,b21,b22,b23,b31,b32,b33,b41,b42,b43
                matC = admin.arange(1,13).reshape(4,3)
                matC.flat[[0,1,2,3,4,5,6,7,8,9,10,11]] = a11-b11,a12-b12,a13-b13,a21-b21,a22-b22,a23-b23,a31-b31,a32-b32,a33-b33,a41-b41,a42-b42,a43-b43
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #E12---------
            elif asc == '3,4':
                a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a34 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a24 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                a34 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b14 b21 to b34 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b14 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b24 = int(input())
                b31 = int(input())
                b32 = int(input())
                b33 = int(input())
                b34 = int(input())
                #HANDLER---------
                matA = admin.arange(1,13).reshape(3,4)
                matA.flat[[0,1,2,3,4,5,6,7,8,9,10,11]] = a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34
                matB = admin.arange(1,13).reshape(3,4)
                matB.flat[[0,1,2,3,4,5,6,7,8,9,10,11]] = b11,b12,b13,b14,b21,b22,b23,b24,b31,b32,b33,b34
                matC = admin.arange(1,13).reshape(3,4)
                matC.flat[[0,1,2,3,4,5,6,7,8,9,10,11]] = a11-b11,a12-b12,a13-b13,a14-b14,a21-b21,a22-b22,a23-b23,a24-b24,a31-b31,a32-b32,a33-b33,a34-b34
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #E13---------
            elif asc == '4,2':
                a11 = int(input('''Please enter a11 a12 a21 to a42 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a21 = int(input())
                a22 = int(input())
                a31 = int(input())
                a32 = int(input())
                a41 = int(input())
                a42 = int(input())
                b11 = int(input('''Please enter b11 b12 a21 to b42 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b21 = int(input())
                b22 = int(input())
                b31 = int(input())
                b32 = int(input())
                b41 = int(input())
                b42 = int(input())
                #HANDLER---------
                matA = admin.arange(1,9).reshape(4,2)
                matA.flat[[0,1,2,3,4,5,6,7]] = a11,a12,a21,a22,a31,a32,a41,a42
                matB = admin.arange(1,9).reshape(4,2)
                matB.flat[[0,1,2,3,4,5,6,7]] = b11,b12,b21,b22,b31,b32,b41,b42
                matC = admin.arange(1,9).reshape(4,2)
                matC.flat[[0,1,2,3,4,5,6,7]] = a11-b11,a12-b12,a21-b21,a22-b22,a31-b31,a32-b32,a41-b41,a42-b42
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #E14---------
            elif asc == '2,4':
                a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a24 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a24 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b14 b21 to b24 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b14 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b24 = int(input())
                #HANDLER---------
                matA = admin.arange(1,9).reshape(2,4)
                matA.flat[[0,1,2,3,4,5,6,7]] = a11,a12,a13,a14,a21,a22,a23,a24
                matB = admin.arange(1,9).reshape(2,4)
                matB.flat[[0,1,2,3,4,5,6,7]] = b11,b12,b13,b14,b21,b22,b23,b24
                matC = admin.arange(1,9).reshape(2,4)
                matC.flat[[0,1,2,3,4,5,6,7]] = a11-b11,a12-b12,a13-b13,a14-b14,a21-b21,a22-b22,a23-b23,a24-b24
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #E15---------
            elif asc == '4,4':
                a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a44 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a24 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                a34 = int(input())
                a41 = int(input())
                a42 = int(input())
                a43 = int(input())
                a44 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b14 b21 to b44 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b14 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b24 = int(input())
                b31 = int(input())
                b32 = int(input())
                b33 = int(input())
                b34 = int(input())
                b41 = int(input())
                b42 = int(input())
                b43 = int(input())
                b44 = int(input())
                #HANDLER---------
                matA = admin.arange(1,17).reshape(4,4)
                matA.flat[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]] = a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34,a41,a42,a43,a44
                matB = admin.arange(1,17).reshape(4,4)
                matB.flat[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]] = b11,b12,b13,b14,b21,b22,b23,b24,b31,b32,b33,b34,b41,b42,b43,b44
                matC = admin.arange(1,17).reshape(4,4)
                matC.flat[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]] = a11-b11,a12-b12,a13-b13,a14-b14,a21-b21,a22-b22,a23-b23,a24-b24,a31-b31,a32-b32,a33-b33,a34-b34,a41-b41,a42-b42,a43-b43,a44-b44
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #E16----------
            else:
                print('''Dimension error--
 --Addition can only be performed with matrix of the same dimension.\n''')
        else:
            print('''Dimension error--
 --Operation cannot be performed with given matrix.\n''')
#--------------------------------------------------------------------------------------------------------------
 #A6--------
#----------------------------| OPERATION 06 |------------------------------------------------------------------

    elif op == '6':
        asd = input("Please enter the dimension of the matA e.g 3,2\n")
        #------ CHECK --------
        if asd == '2,2' or asd == '3,3' or asd == '4,4' or asd == '2,1' or asd == '1,2' or asd == '1,3' or asd == '1,4' or asd == '2,3' or asd == '2,4' or asd == '4,2' or asd == '3,2' or asd == '3,4' or asd == '3,1' or asd == '4,1' or asd == '4,2' or asd == '4,3' :
            asc = input("Please enter the dimension of the matB e.g 3,2\n")
            #D1--------
            if asc == '2,2' and asd == '2,2':
                a11 = int(input('''Please enter a11 a12 a21 a22 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a21 = int(input())
                a22 = int(input())
                b11 = int(input('''Please enter b11 b12 b21 b22 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b21 = int(input())
                b22 = int(input())
                #HANDLER---------
                matA = admin.arange(1,5).reshape(2,2)
                matA.flat[[0,1,2,3]] = a11,a12,a21,a22
                matB = admin.arange(1,5).reshape(2,2)
                matB.flat[[0,1,2,3]] = b11,b12,b21,b22
                matC = admin.arange(1,5).reshape(2,2)
                matC.flat[[0,1,2,3]] = a11-b11,a12-b12,a21-b21,a22-b22
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #D2---------
            elif asc == '2,3' and asd == '3,2':
                a11 = int(input('''Please enter a11 a12 a13 a21 a22 a23 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b21 b22 b23 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                #HANDLER---------
                matA = admin.arange(1,7).reshape(2,3)
                matA.flat[[0,1,2,3,4,5]] = a11,a12,a13,a21,a22,a23
                matB = admin.arange(1,7).reshape(2,3)
                matB.flat[[0,1,2,3,4,5]] = b11,b12,b13,b21,b22,b23
                matA = admin.arange(1,7).reshape(2,3)
                matA.flat[[0,1,2,3,4,5]] = a11-b11,a12-b12,a13-b13,a21-b21,a22-b22,a23-b23
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #D3---------
            elif asc == '3,2' and asd == '2,3':
                a11 = int(input('''Please enter a11 a12 a21 a22 a31 a32 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a21 = int(input())
                a22 = int(input())
                a31 = int(input())
                a32 = int(input())
                b11 = int(input('''Please enter b11 b12 b21 b22 b31 b32 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b21 = int(input())
                b22 = int(input())
                b31 = int(input())
                b32 = int(input())
                #HANDLER---------
                matA = admin.arange(1,7).reshape(3,2)
                matA.flat[[0,1,2,3,4,5]] = a11,a12,a21,a22,a32,a32
                matB = admin.arange(1,7).reshape(3,2)
                matB.flat[[0,1,2,3,4,5]] = b11,b12,b21,b22,b32,b32
                matC = admin.arange(1,7).reshape(3,2)
                matC.flat[[0,1,2,3,4,5]] = a11-b11,a12-b12,a21-b21,a22-b22,a31-b31,a32-b32
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #D4---------
            elif asc == '3,3' and asd == '3,3':
                a11 = int(input('''Please enter a11 a12 a13 a21 to a33 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b21 to b33 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b31 = int(input())
                b32 = int(input())
                b33 = int(input())
                #HANDLER---------
                matA = admin.arange(1,10).reshape(3,3)
                matA.flat[[0,1,2,3,4,5,6,7,8]] = a11,a12,a13,a21,a22,a23,a31,a32,a33
                matB = admin.arange(1,10).reshape(3,3)
                matB.flat[[0,1,2,3,4,5,6,7,8]] = b11,b12,b13,b21,b22,b23,b31,b32,b33
                matC = admin.arange(1,10).reshape(3,3)
                matC.flat[[0,1,2,3,4,5,6,7,8]] = a11-b11,a12-b12,a13-b13,a21-b21,a22-b22,a23-b23,a31-b31,a32-b32,a33-b33
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #D5----------
            elif asc == '2,1' and asd == '1,2' :
                a11 = int(input('''Please enter a11 and a21 of matA respectively--
 --Pressing enter after each input.\n'''))
                a21 = int(input())
                b11 = int(input('''Please enter b11 and b21 of matB respectively--
 --Pressing enter after each input.\n'''))
                b21 = int(input())
                #HANDLER---------
                matA = admin.arange(1,3).reshape(2,1)
                matA.flat[[0,1]] = a11,a21
                matB = admin.arange(1,3).reshape(2,1)
                matB.flat[[0,1]] = b11,b21
                matC = admin.arange(1,3).reshape(2,1)
                matC.flat[[0,1]] = a11-b11,a21-b21
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #D6---------
            elif asc == '3,1' and asd == '1,3':
                a11 = int(input('''Please enter a11 a21 and a31 of matA respectively--
 --Pressing enter after each input.\n'''))
                a21 = int(input())
                a31 = int(input())
                b11 = int(input('''Please enter b11 b21 and b31 of matB respectively--
 --Pressing enter after each input.\n'''))
                b21 = int(input())
                b31 = int(input())
                #HANDLER---------
                matA = admin.arange(1,4).reshape(3,1)
                matA.flat[[0,1,2]] = a11,a21,a31
                matB = admin.arange(1,4).reshape(3,1)
                matB.flat[[0,1,2]] = b11,b21,b31
                matC = admin.arange(1,4).reshape(3,1)
                matC.flat[[0,1,2]] = a11-b11,a21-b21,a31-b31
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #D7---------
            elif asc == '1,2' and asd == '2,1':
                a11 = int(input('''Please enter a11 and a12 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                b11 = int(input('''Please enter b11 and b12 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                #HANDLER---------
                matA = admin.arange(1,3).reshape(1,2)
                matA.flat[[0,1]] = a11,a12
                matB = admin.arange(1,3).reshape(1,2)
                matB.flat[[0,1]] = b11,b12
                matC = admin.arange(1,3).reshape(1,2)
                matC.flat[[0,1]] = a11-b11,a12-b12
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #D8---------
            elif asc == '1,3' and asd == '3,1':
                a11 = int(input('''Please enter a11 a12 and a13 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                b11 = int(input('''Please enter b11 b12 and b13 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                #HANDLER---------
                matA = admin.arange(1,4).reshape(1,3)
                matA.flat[[0,1,2]] = a11,a12,a13
                matB = admin.arange(1,4).reshape(1,3)
                matB.flat[[0,1,2]] = b11,b12,b13
                matC = admin.arange(1,4).reshape(1,3)
                matC.flat[[0,1,2]] = a11-b11,a12-a12,a13-a13
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #D9---------
            elif asc == '1,4' and asd == '4,1':
                a11 = int(input('''Please enter a11 a12 a13 and a14 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 and a14 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b14 = int(input())
                #HANDLER---------
                matA = admin.arange(1,5).reshape(1,4)
                matA.flat[[0,1,2,3]] = a11,a12,a13,a14
                matA = admin.arange(1,5).reshape(1,4)
                matA.flat[[0,1,2,3]] = b11,b12,b13,b14
                matA = admin.arange(1,5).reshape(1,4)
                matA.flat[[0,1,2,3]] = a11-b11,a12-b12,a13-b13,a14-b14
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #E10---------
            elif asc == '4,1' and asd == '1,4':
                a11 = int(input('''Please enter a11 a21 a31 and a41 of matA respectively--
 --Pressing enter after each input.\n'''))
                a21 = int(input())
                a31 = int(input())
                a41 = int(input())
                b11 = int(input('''Please enter b11 b21 b31 and b41 of matB respectively--
 --Pressing enter after each input.\n'''))
                b21 = int(input())
                b31 = int(input())
                b41 = int(input())
                #HANDLER---------
                matA = admin.arange(1,5).reshape(4,1)
                matA.flat[[0,1,2,3]] = a11,a21,a31,a41
                matB = admin.arange(1,5).reshape(4,1)
                matB.flat[[0,1,2,3]] = b11,b21,b31,b41
                matC = admin.arange(1,5).reshape(4,1)
                matC.flat[[0,1,2,3]] = a11-b11,a21-b21,a31-b31,a41-b41
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #E11---------
            elif asc == '4,3' and asd == '3,4':
                a11 = int(input('''Please enter a11 a12 a13 a21 to a43 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                a41 = int(input())
                a42 = int(input())
                a43 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b21 to b43 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b31 = int(input())
                b32 = int(input())
                b33 = int(input())
                b41 = int(input())
                b42 = int(input())
                b43 = int(input())
                #HANDLER---------
                matA = admin.arange(1,13).reshape(4,3)
                matA.flat[[0,1,2,3,4,5,6,7,8,9,10,11]] = a11,a12,a13,a21,a22,a23,a31,a32,a33,a41,a42,a43
                matB = admin.arange(1,13).reshape(4,3)
                matB.flat[[0,1,2,3,4,5,6,7,8,9,10,11]] = b11,b12,b13,b21,b22,b23,b31,b32,b33,b41,b42,b43
                matC = admin.arange(1,13).reshape(4,3)
                matC.flat[[0,1,2,3,4,5,6,7,8,9,10,11]] = a11-b11,a12-b12,a13-b13,a21-b21,a22-b22,a23-b23,a31-b31,a32-b32,a33-b33,a41-b41,a42-b42,a43-b43
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #E12---------
            elif asc == '3,4' and asd == '4,3':
                a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a34 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a24 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                a34 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b14 b21 to b34 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b14 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b24 = int(input())
                b31 = int(input())
                b32 = int(input())
                b33 = int(input())
                b34 = int(input())
                #HANDLER---------
                matA = admin.arange(1,13).reshape(3,4)
                matA.flat[[0,1,2,3,4,5,6,7,8,9,10,11]] = a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34
                matB = admin.arange(1,13).reshape(3,4)
                matB.flat[[0,1,2,3,4,5,6,7,8,9,10,11]] = b11,b12,b13,b14,b21,b22,b23,b24,b31,b32,b33,b34
                matC = admin.arange(1,13).reshape(3,4)
                matC.flat[[0,1,2,3,4,5,6,7,8,9,10,11]] = a11-b11,a12-b12,a13-b13,a14-b14,a21-b21,a22-b22,a23-b23,a24-b24,a31-b31,a32-b32,a33-b33,a34-b34
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #E13---------
            elif asc == '4,2' and asd == '2,4':
                a11 = int(input('''Please enter a11 a12 a21 to a42 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a21 = int(input())
                a22 = int(input())
                a31 = int(input())
                a32 = int(input())
                a41 = int(input())
                a42 = int(input())
                b11 = int(input('''Please enter b11 b12 a21 to b42 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b21 = int(input())
                b22 = int(input())
                b31 = int(input())
                b32 = int(input())
                b41 = int(input())
                b42 = int(input())
                #HANDLER---------
                matA = admin.arange(1,9).reshape(4,2)
                matA.flat[[0,1,2,3,4,5,6,7]] = a11,a12,a21,a22,a31,a32,a41,a42
                matB = admin.arange(1,9).reshape(4,2)
                matB.flat[[0,1,2,3,4,5,6,7]] = b11,b12,b21,b22,b31,b32,b41,b42
                matC = admin.arange(1,9).reshape(4,2)
                matC.flat[[0,1,2,3,4,5,6,7]] = a11-b11,a12-b12,a21-b21,a22-b22,a31-b31,a32-b32,a41-b41,a42-b42
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #E14---------
            elif asc == '2,4' and asd == '4,2':
                a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a24 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a24 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b14 b21 to b24 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b14 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b24 = int(input())
                #HANDLER---------
                matA = admin.arange(1,9).reshape(2,4)
                matA.flat[[0,1,2,3,4,5,6,7]] = a11,a12,a13,a14,a21,a22,a23,a24
                matB = admin.arange(1,9).reshape(2,4)
                matB.flat[[0,1,2,3,4,5,6,7]] = b11,b12,b13,b14,b21,b22,b23,b24
                matC = admin.arange(1,9).reshape(2,4)
                matC.flat[[0,1,2,3,4,5,6,7]] = a11-b11,a12-b12,a13-b13,a14-b14,a21-b21,a22-b22,a23-b23,a24-b24
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #E15---------
            elif asc == '4,4' and asd == '4,4':
                a11 = int(input('''Please enter a11 a12 a13 a14 a21 to a44 of matA respectively--
 --Pressing enter after each input.\n'''))
                a12 = int(input())
                a13 = int(input())
                a14 = int(input())
                a21 = int(input())
                a22 = int(input())
                a23 = int(input())
                a24 = int(input())
                a31 = int(input())
                a32 = int(input())
                a33 = int(input())
                a34 = int(input())
                a41 = int(input())
                a42 = int(input())
                a43 = int(input())
                a44 = int(input())
                b11 = int(input('''Please enter b11 b12 b13 b14 b21 to b44 of matB respectively--
 --Pressing enter after each input.\n'''))
                b12 = int(input())
                b13 = int(input())
                b14 = int(input())
                b21 = int(input())
                b22 = int(input())
                b23 = int(input())
                b24 = int(input())
                b31 = int(input())
                b32 = int(input())
                b33 = int(input())
                b34 = int(input())
                b41 = int(input())
                b42 = int(input())
                b43 = int(input())
                b44 = int(input())
                #HANDLER---------
                matA = admin.arange(1,17).reshape(4,4)
                matA.flat[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]] = a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34,a41,a42,a43,a44
                matB = admin.arange(1,17).reshape(4,4)
                matB.flat[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]] = b11,b12,b13,b14,b21,b22,b23,b24,b31,b32,b33,b34,b41,b42,b43,b44
                matC = admin.arange(1,17).reshape(4,4)
                matC.flat[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]] = a11-b11,a12-b12,a13-b13,a14-b14,a21-b21,a22-b22,a23-b23,a24-b24,a31-b31,a32-b32,a33-b33,a34-b34,a41-b41,a42-b42,a43-b43,a44-b44
                #Output----------
                print('matA:\n',matA)
                print('\nmatB:\n',matB)
                print('\nDifference: \n',matC,'\n\n')
            #E16----------
            else:
                print('''Dimension error--
 --Addition can only be performed with matrix of the same dimension.\n''')
        else:
            print('''Dimension error--
 --Operation cannot be performed with given matrix.\n''')
#--------------------------------------------------------------------------------------------------------------
 #A7--------
#----------------------------| OPERATION 07 |------------------------------------------------------------------

    elif op == '7':
        asd = input("Please enter the dimension of matA e.g 2,3\n")

        if asd == '2,2':
            asd = input("Please enter the dimension of matB e.g 3,2\n")
            matA = admin.arange(1,7)
            matB = admin.arange(1,7)
        elif asd == '2,3':
            asd = input("Please enter the dimension of matB e.g 3,2\n")
        elif asd == '3,2':
            asd = input("Please enter the dimension of matB e.g 3,2\n")
        elif asd == '3,3':
            asd = input("Please enter the dimension of matB e.g 3,2\n")
        elif asd == '2,1':
            asd = input("Please enter the dimension of matB e.g 3,2\n")
        elif asd == '3,1':
            asd = input("Please enter the dimension of matB e.g 3,2\n")
        else:
            print('''\nInvalid matrix dimension--
 --please check your input and try again!\n\n''')
#--------------------------------------------------------------------------------------------------------------
    #A8----------
#----------------------------| EXCEPTION |---------------------------------------------------------------------
    else:
        print('''\nOperation not recognized--
 --please check your input and try again!\n\n''')
    
