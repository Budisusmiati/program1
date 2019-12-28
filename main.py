from view.view_nilai import search,cetak,header,notoption
from view.input_nilai import inputan,edit,delete
header()
while True:

    c = input("\nPilih MENU: ")

    # KELUA PROGRAM
    if c.lower() == 'q':
        print(".:======TERIMAKASIH======:.")
        ext = input("\nPress ENTER to exit")
        if ext == '':
            break
        else:
            break

    # TAMPILKAN LIST DATA
    elif c.lower() == 'l':
        cetak()

    # UNTUK MENAMBAH DATA
    elif c.lower() == 'a':
        inputan()

    # EDIT DATA
    elif c.lower() == 'e':
        edit()

    # MENCARI DATA
    elif c.lower() == 's':
        search()

    # HAPUS DATA
    elif c.lower() == 'd':
        delete()

    else:
        notoption()