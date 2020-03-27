#création de l'aliment

def creation_aliment(tipe):
    if tipe == "fruit":
        poid = 1
        return {"tipe": tipe,"poid": poid}
    
    elif tipe == "legume":
        poid = 3
        return {"tipe": tipe,"poid": poid}

    elif tipe == "proteine":
        poid = 7
        return {"tipe": tipe,"poid": poid}

    else:
        print("erreure l'aliment n'est pas pris en compte")
