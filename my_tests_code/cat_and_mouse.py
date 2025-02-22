def catAndMouse(x:int, y:int, z:int)->str:
    linea = abs(z-x)
    lineb = abs(z-y)
    if linea<lineb:
        return 'Cat A'
    elif linea>lineb:
        return 'Cat B'
    else:
        return 'Mouse C'
    
if __name__ == '__main__':
    line_str = input('Enter A B C: ')
    line = map(int, line_str.split())
    result = catAndMouse(*line)
    print('Result:',result)