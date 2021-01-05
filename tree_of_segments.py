def build(array):
    tree = [0] * 4 * (len(array) + 1)


    def buid_tree(v, tl, tr):
        if tl == tr:
            tree[v] = array[tl]
        else:
            buid_tree(v * 2, tl, (tl + tr) // 2)
            buid_tree(v * 2 + 1, (tl + tr) // 2 + 1, tr)
            tree[v] = tree[v * 2]  + tree[v * 2 + 1]
    

    buid_tree(1, 0, len(array) - 1)
    return tree


def get_sum(tree, n, left, right):
    def sum(v, tl, tr):
        if left <= tl and tr <= right:
            return tree[v]
        if tr < left or right < tl:
            return 0
        return (sum(v * 2, tl, (tl + tr) / 2) +
                sum(v * 2 + 1, (tl + tr) / 2 + 1, tr))
    

    return sum(1, 0, n - 1)


def update_tree(tree, n, pos, val):
    def update(v, tl, tr):
        if tr == tr:
            t[v] = val
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                update(v * 2,  tl, tm)
            else:
                update(v * 2 + 1, tm + 1, tr)
            t[v] = t[v * 2] + t[v * 2 + 1]
    
    update(1, 0, n - 1)
    
    
