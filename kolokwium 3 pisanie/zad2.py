#Marcin Mikuła

#Opis rozwiązania:
#Rozwiązanie polega na przechowywaniu w węzłach wartości minimalnej z dzieci danego węzła, (o ile dzieci nie są liścmi)
# i wartości w danym węźle. Wartośc ta oznacza minimalny koszt odcięcia liści od korzenia dla danego poddrzewa
#Żeby zliczyć wartości minimalne za pomocą dodatkowego wskaźnika funkcja rekurencyjnie schodzi aż do liści, następnie przechodzi do
#rodzica rodzica i stamtąd rozpoczyna zliczanie i edytuje wartości trzymane w podkorzeniach, aż dojdzie do korzenia całego drzewa. Minimalna suma wartości wierzchołków jaką
#należy usunąć z drzewa żeby odciąć połączenie korzeń - liście jest suma dzieci korzenia całego drzewa

from zad2testy import runtests

class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def cutthetree(T):
        def rekur(T, curT):
            if curT.left != None: rekur(T, curT.left)
            if curT.right != None: rekur(T, curT.right)


            if curT.parent != None:
                if curT.parent.parent != None:
                    tmp = curT.parent.parent

                    if tmp.left != None and tmp.right == None:
                        tmp.value = min((tmp.left.value), tmp.value)

                    elif tmp.right != None and tmp.left == None:
                        tmp.value = min((tmp.right.value), tmp.value)

                    else:
                        tmp.value = min((tmp.right.value + tmp.left.value), tmp.value)

                    if tmp.parent == None:

                        if tmp.left != None and tmp.right == None:
                            tmp.value = tmp.left

                        elif tmp.right != None and tmp.left == None:
                            tmp.value = tmp.right

                        else:
                            tmp.value = tmp.right.value + tmp.left.value

            return (T.value)

        return rekur(T, T)

    
runtests(cutthetree)


