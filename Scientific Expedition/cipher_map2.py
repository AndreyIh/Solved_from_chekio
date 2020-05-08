#!/usr/bin/env checkio --domain=py run cipher-map2

# 
# END_DESC

def rotate_m(mat):
    """Rotates the matrix to the right"""
    a1 = ['','','','']
    for i in mat:
        m = -1
        for j in i:
            m += 1
            a1[m] = j + a1[m]
    
    return a1
 
def recall_password(template, cipher):
    password = ''
    for n in range (0, 4):
        for i in range(0, 4):
            for j in range(0,4):
                if template[i][j] == 'X':
                    password += cipher[i][j]
        template = rotate_m(template)
      
    return password



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'