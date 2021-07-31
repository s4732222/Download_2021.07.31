import math


def td(T,RH):
    r=(17.27*T/(237.7+T)+math.log(RH/100))
    Td=237.7*r/(17.27-r)
    return Td
'''
Td=td(10.9,64)
print(Td)
'''

def Mechanical_mixing_height(T,Td,Pasquill,Uz,Z,Z0):
    mechanical_mixing_height=(121/6)*(6-Pasquill)*(T-Td)+0.169*Pasquill*(Uz+0.257)/12*0.0000579*math.log(Z/Z0)
    return mechanical_mixing_height

'''
print(Mechanical_mixing_height(10.9,Td,3,2.6,14,1.2))
'''


def Uv_value(uv,Uz):

    if uv>float(0.8) and Uz<float(2):
        a='等級A'
        print('1')
    elif uv>float(0.8) and float(2)<=Uz<=float(5):
        b='等級B'
        print('2')
    elif uv>float(0.8) and Uz>float(5):
        c='等級C'
        print('3')
    elif float(0.4)<uv<=float(0.8) and Uz<float(3):
        b='等級B'
        print('2')
    elif float(0.4)<uv<=float(0.8) and float(3)<=Uz<=float(5):
        c='等級C'
        print('3')
    elif float(0.4)<uv<=float(0.8) and Uz>float(5):
        d='等級D'
        print('4')
    elif float(0.1)<uv<=float(0.4)and Uz<float(2):
        b='等級B'
        print('2')
    elif float(0.1)<uv<=float(0.4)and float(2)<=Uz<=float(5):
        c='等級C'
        print('3')
    elif float(0.1)<uv<=float(0.4)and Uz>float(5):
        d='等級D'
        print('4')
    elif uv<float(0.1)and Uz<float(2):
        f='等級F'
        print('6')
    elif uv<float(0.1)and float(2)<=Uz<=float(3):
        e='等級E'
        print('5')
    elif uv<float(0.1)and Uz>float(3):
        d='等級D'
        print('4')
    else:
        print('Error')
    return uv,Uz
'''
    if (a=='等級A',b=='等級B',c=='等級C',d=='等級D',e=='等級E',f=='等級F'):
        a=1
        b=2
        c=3
        d=4
        e=5
        f=6

    else:
        print('Error')
    
'''
print(Uv_value(1,3))




