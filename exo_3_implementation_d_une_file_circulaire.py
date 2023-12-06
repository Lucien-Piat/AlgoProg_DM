#DM Algoprog Exercice 3, File circulaire : 

def creer_file(capacite):
    """
    Retourne une file vide de capacitée maximale 'capacite'.
    capacite : un entier
    
    >>> file = creer_file(3)
    >>> print(file)
    ['*', None, None, None]
    
    """
    return ['*']+[None] * capacite

def file_est_vide(f):
    """
    Renvoie Vrai si la file est vide 
    
    f : une file
    
    >>> file_est_vide([3, 4, 5, '*'])
    
    
    >>> file_est_vide(['*', None, None, None])
    True
    
    """    
    if f.count(None) == len(f)-1 : return True 

def file_est_pleine(f):
    """
    Renvoie Vrai si la file est pleine
    
    f : une file
    
    >>> file_est_pleine([3, 4, 5, '*'])
    True
    
    >>> file_est_pleine(['*', None, None, None])

    """    
    if f.count(None) == 0 : return True 

def enfiler(f, e):
    """
    Ajoute l'élément 'e' dans la file 'f'
    Si la file est pleine, l'élément n'est pas enfilé dans la file. 
    
    La fonction retourne vrai en cas de succes et faux sinon
    
    f : une file
    e : un element
    
    >>> lst = ['*', None, None, None]
    >>> enfiler(lst,3)
    True
    >>> print(lst)
    ['*', None, None, 3]
    >>> enfiler(lst,4)
    True
    >>> print(lst)
    ['*', None, 4, 3]
    
    >>> lst = [None, 5, '*', None]
    >>> enfiler(lst,3)
    True
    >>> print(lst)
    [3, 5, '*', None]
    
    >>> lst = [3, 4, 5, '*']
    >>> enfiler(lst,3)
    
    >>> print(lst)
    [3, 4, 5, '*']
    
    """
    if file_est_pleine(f) : return
    for i in range(len(f)):
        if f[i] == "*":
            f[(f.count(None) + i ) - len(f)]=e
            return True 

def defiler(f): 
    """
    Retire le dernier élément de la file 'f' et le renvoie. 
    Si la file est vide, la foncion renvoie None
    
    f : une file
    e : un element 
    
    >>> lst = ['*', None, None, None]
    >>> defiler(lst)
    
    >>> lst = [3, 5, '*', 10]
    >>> defiler(lst)
    10
    >>> defiler(lst)
    3
    >>> print(lst)
    [None, 5, '*', None]
    
    >>> lst = ['*', None, 5, 10]
    >>> defiler(lst)
    5
        
    """
    if file_est_vide(f): return 
    
    for i in range(len(f)):
        if f[i] == '*':
            for y in range(len(f)):
                if f[i-(y+1)] == '*' or f[i-(y+1)] == None :
                    pop, f[i-y] = f[i-y], None
                    return pop
                
def inserer_file(f, e):
    """
    Ajoute l'élement e dans la file.
    
    Si, au moment d'ajouter en la file est pleine, cette fonction
    double sa capacité anvant d'effectuer l'opération.
    
    f : une file
    e : un element
    
    """
    if file_est_pleine(f):
        redimentionner_file(f, len(f)*2-2)
    enfiler(f, e)
     
def redimentionner_file(f, capacite):
    """
    Redimentionne la capacité de f de sorte que la capacité de f
    devienne égale à la 'capacite', si c'est possible.
    
    En cas de succés, la fonction renvoie Vrai. 
    En cas d'échec (quand la taille de al file est plus grande que
    la noucelle capacité), la file n'est pas modifiée et la
    fonction renvoie Faux.
    
    Alternative au insert (porblèmes d'espace mémoire) :
    f = f[:i+1] +  ([None]*(capacite+1 - len(f))) + f[i+1:]   
    
    f : une file 
    
    capacité : un entier
    
    >>> lst = [3, 4, 5, '*']
    >>> redimentionner_file(lst, 7)
    True
    >>> print(lst)
    [3, 4, 5, '*', None, None, None, None]
    
    >>> lst = [3, 4, 5, '*']
    >>> redimentionner_file(lst, 2)
    False

    >>> lst = [3, 4, 5, '*']
    >>> redimentionner_file(lst, 3)
    True
    >>> print(lst)
    [3, 4, 5, '*']
    
    """
    if len(f) > capacite+1 : 
        return False
    for i in range(len(f)):
        if f[i] == "*":
            for y in range(capacite+1 - len(f)):
                f.insert(i+1, None)
            return True
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
