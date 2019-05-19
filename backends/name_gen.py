"""Random fantasy name generator"""

def name(race,gender):
    name=""
    if gender == "m":
        if race == "dwarf":
            onset = [["",10],["k",8],["p",6],["q",2],["g",9],["ts",5],["t",7],["x",7],["kr",4],["gt",5],["kl",4],["d",5],["dl",3],["t-h",5],["jf",7],["ks",6],["bz",4],["gp",7],["gf",6],["br",7],["dr",8],["tl",4],["td",7],["sd",2],["l",1]]
            nucleas = [["a",10],["o",30],["e",10],["oa",5],["oe",6],["ao",2],["ea",1],["ae",2],["u",30],["uo",12],["ou",10],["au",5],["ua",10],["uɂu",20],["oɂo",20]]
            coda = [["ls",10],["wk",9],["lk",6],["p",6],["b",6],["k",9],["dk",3],["g",7],["ng",6],["",20]]

            options = [1,2]
            cyl = r.choices(options, weights=[10,2])[0]
        
        elif race == "elf":

            onset = [["",20],["s",10],["r",10],["v",10],["f",10],["h",10],["l",10],["rr",5],["bb",5],["z",10],["m",10],["n",10],["hf",6],["fh",6],["sz",2],["shw",5],["ln",5],["vl",3],["zs",2],["hz",4],["hv",3],["vf",2],["hr",5],["hrr",3],["pp",3],["ppr",2],["bbr",2],["rrs",3],["pps",5],["ppv",2],["bbv",5],["ppf",5],["bbz",5],["bbs",4],["bbn",5],["ppn",4],["hs",7],["hm",5],["sw",4],["fn",4],["sn",4],["shs",5],["shz",3],["zhm",4],["zh",5],["zhl",4],["zhn",4],["ls",5],["bbl",5],["rrl",5],["rrn",5],["rn",7],["vw",4],["lv",5],["nl",6],["nm",5],["mn",5],["zv",2],["lr",4],["rrv",4],["hl",5],["sw",4],["s-h",4],["ml",5],["bbrr",3],["fw",3],["bbm",3],["wn",4],["mw",3],["ms",4],["zhf",4],["frr",5],["mbb",2],["wrr",5],["w",10],["zhs",5]]
            nucleas = [["a",5],["e",8],["i",7],["o",3],["u",3],["ae",9],["ai",10],["ao",6],["au",5],["ea",8],["ei",7],["eo",5],["eu",8],["ia",6],["ie",9],["io",6],["iu",8],["oa",10],["oe",8],["oi",5],["ou",6],["ua",6],["ue",3],["ui",5],["uo",1]]
            coda = [["",10],["l",9],["b",7],["rl",9],["rr",8],["g",6],["k",1],["t",5],["d",5],["r",9],["y",7],["rh",6],["h",7]]

            options = range(1, 10)
            cyl = r.choices(options, weights=[60, 5, 5, 5, 5, 5, 5, 5, 1])[0]


        elif race == "human":
            onset = [["",10],["g",5],["d",8],["t",4],["k",6],["p",2],["b",5],["n",5],["m",5],["s",5],["l",5],["w",5],["r",5],["h",3],["j",6],["r",6]]
            nucleas = [["a",12],["e",10],["i",8],["o",10],["u",9]]
            coda = [["w",5],["s",5],["r",5],["h",1],["l",5],["p",3],["rl",1]]
            options = range(1, 4)
            cyl = r.choices(options, weights=[2,4,1])[0]
            if r.choices(options, weights=[6,5,5])[0] < 2:
                if r.randint(1,2) == 1:
                   name +="y"
                else:
                    name+="ie"
        

        elif race == Gnome:
            pass
        elif race == Halfling:
            pass
        elif race == Half-Orc:
            pass
        elif race == Dragonborn:
            pass
        elif race == Tiefling:
            pass
        elif race == Goblin:
            pass
        elif race == Orc:
            pass
          
        for x in range(0,cyl):
          name += r.choices(onset, weights=[l[1] for l in onset])[0][0]
          name += r.choices(nucleas, weights=[l[1] for l in nucleas])[0][0]
          name += r.choices(coda, weights=[l[1] for l in coda])[0][0]
        
        if race == "human":
          if r.choices([1,2,3], weights=[6,5,5])[0] < 2:
                if r.randint(1,2) == 1:
                   name +="y"
                else:
                    name+="ie"
        return name
