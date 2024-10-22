import ABR

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    t = ABR.Abr(20)
    t.insert(15)
    t.insert(6)
    t.insert(7)
    t.insert(25)
    t.insert(8)
    t.insert(16)
    print(t.inorder())
    t.search(12)
    t.min()
    t.delete(15)
