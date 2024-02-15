def ievadiet_savu_vardu():
 teksta_fails = input("ievadiet savu vardu: ")
 return teksta_fails

def izveidot_jaunu_failu(faila_nosaukums, teksta_fails):
 try:
     with open(faila_nosaukums, 'a') as f:
            f.write(teksta_fails + '\n')
     return True
 except IOError:
     return False

def zinot(rezultats):
    if rezultats:
        print("vards tika ierakstits faila!")
    else:
        print("vards netika ierakstits faila.")

if __name__ == "__main__":
    teksta_fails = ievadiet_savu_vardu()
    rezultats = izveidot_jaunu_failu("lietotajs.txt", teksta_fails)
    zinot(rezultats)