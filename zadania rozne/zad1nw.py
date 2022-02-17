class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def print_tree(root, key="key", left="left", right="right"):
    def display(root, key=key, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, key)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, key)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, key)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, key)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, key, left, right)
    for line in lines:
        print(line)


def find(root, key):
    while root != None:
        if root.key == key:
            return root
        elif root.key < key:
            root = root.right
        else:
            root = root.left

    return None


def mini(root):
    while root.left != None:
        root = root.left
    return root
    #return root.key


def maxi(root):
    while root.right != None:
        root = root.right
    return root
    #return root.key


def succ(root):#nastepnik
    #jeżeli dany wierzchołek ma prawe dziecko
    if root.right != None:
        root = root.right
        return mini(root)

    else:
        if root.parent == None:
            return None

        while root.parent != None:
            if root.parent.left == root:
                return root.parent
            root = root.parent

        return None


def pred(root):#poprzednik
    #jeżeli wierzchołek ma lewe dziecko

    if root.left != None:
        root = root.left
        return maxi(root)

    else:
        if root.parent == None:
            return None

        while root.parent != None:
            if root.parent.right == root:
                return root.parent
            root = root.parent

        return None


def insert(root, key):
    #zakładam że root nie jest Nonem, ani jego wartośc nie jest None
    proot = root.parent
    while root != None:
        proot = root
        if root.key == key:
            return False
        elif root.key < key:
            root = root.right
        else:
            root = root.left

    new = BSTNode(key)
    new.parent = proot
    if key > proot.key:
        proot.right = new
    else:
        proot.left = new

    return True


def remove(root, key):
    #jeżeli chcemy usunąc roota
    if root.key == key:
        #jeżeli w drzewie jest tylko root
        if root.left == None and root.right == None:
            root.key = None
            return

        if pred(root) != None:
            tmp = pred(root)
        else:
            tmp = succ(root)

        remove(root, tmp.key)
        root.key = tmp.key
        return True

    root = find(root, key)
    if root == None:
        return False

    #usuwanie elementu z którego wychodzi tylko jedna gałąź
    if root.left != None and root.right == None:
        proot = root.parent
        if proot.right == root:
            proot.right = root.left
        else:
            proot.left = root.left
        root.left.parent = proot
        return True

    # usuwanie elementu z którego wychodzi tylko jedna gałąź
    elif root.right != None and root.left == None:
        proot = root.parent
        if proot.right == root:
            proot.right = root.right

        else:
            proot.left = root.right
        root.right.parent = proot
        return True

    #usuwanie liscia
    elif root.right == None and root.left == None:

        proot = root.parent
        if proot.right == root:
            proot.right = None
        else:
            proot.left = None

        return True

    #usuwanie wierzchołka kiedy wychodzą z niego 2 gałęzie
    else:
        tmp = succ(root)
        root.key = tmp.key
        ptmp = tmp.parent
        if ptmp.left == tmp:
            ptmp.left = None
        elif ptmp.right == tmp:
            ptmp.right = None

        return True



def cutthetree(T, curT):
    if curT.left != None: cutthetree(T, curT.left)
    if curT.right != None: cutthetree(T, curT.right)

    if curT != None and curT.left is None and curT.right is None:

        tmp = curT.parent.parent

        if tmp.left != None and tmp.right == None:
            tmp.key = min((tmp.left.key), tmp.key)

        elif tmp.right != None and tmp.left == None:
            tmp.key = min((tmp.right.key), tmp.key)

        else:
            tmp.key = min((tmp.right.key + tmp.left.key), tmp.key)


        if tmp.parent == None:

            if tmp.left != None and tmp.right == None:
                tmp.key = tmp.left

            elif tmp.right != None and tmp.left == None:
                tmp.key = tmp.right

            else:
                tmp.key = tmp.right.key + tmp.left.key

    else:
        if curT.parent != None:
            if curT.parent.parent != None:
                tmp = curT.parent.parent

                if tmp.left != None and tmp.right == None:
                    tmp.key = min((tmp.left.key), tmp.key)

                elif tmp.right != None and tmp.left == None:
                    tmp.key = min((tmp.right.key), tmp.key)

                else:
                    tmp.key = min((tmp.right.key + tmp.left.key), tmp.key)

                if tmp.parent == None:

                    if tmp.left != None and tmp.right == None:
                        tmp.key = tmp.left

                    elif tmp.right != None and tmp.left == None:
                        tmp.key = tmp.right

                    else:
                        tmp.key = tmp.right.key + tmp.left.key


    return (T.key)





#drzewko z wykładu
root = BSTNode(5)

insert(root, 6)
insert(root, 7)
insert(root, 10)
insert(root, 8)
insert(root, 11)
insert(root, 3)
insert(root, -1)
insert(root, -5)
insert(root, -10)
insert(root, -2)



# remove(root, 21)
# remove(root, 20)
# remove(root, 37)
# remove(root, 25)
# remove(root, 40)
# remove(root, 15)
# remove(root, 13)
# remove(root, 6)
print_tree(root)
print(cutthetree(root, root))
print_tree(root)
# print(succ(root))