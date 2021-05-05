import numpy as np
def funkcja(m,n):
    numrows = len(m)
    numcols = len(m[0])
    if(n == "pion" and numcols % 2 != 0):
        return "Błędna liczba kolumn."
    if(n == "poziom" and numrows % 2 != 0):
        return "Błędna liczba wierszy."
    if(n == "pion" and numcols % 2 == 0):
        b_col = a[:, 0:int(numcols/2)]
        c_col = a[:, int(numcols/2):]
        return b_col, c_col
    if(n == "poziom" and numrows % 2 == 0):
        b_row = a[0:int(numrows/2), :]
        c_row = a[int(numrows/2):, :]
        return b_row, c_row

a = np.array([[0,1,1,1],[2,3,1,1],[1,2,3,4],[4,3,2,1]])
print(funkcja(a,"pion"))