import ABR

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    t = ABR.Abr(20)
    t.insert(15)
    t.insert(6)
    t.insert(7)
    t.insert(55)
    t.insert(8)
    t.insert(16)
    t.insert(21)
    t.insert(28)
    t.insert(22)
    print(t.inorder())
    t.search(12)
    t.min()
    print(t.inorder())
    t.get_kesimo(3)
    t.size()
    print(t.height())
