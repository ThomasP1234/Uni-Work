def getCubes(maxSize, numberToGenerate):
    cubes = []
    for d in range(1,maxSize):
        cubeD=d**3
        for c in range(1,d):
            cubeC=c**3
            for b in range(1,c):
                cubeB=b**3
                for a in range(1,b):
                    cubeA=a**3
                    if (cubeD==cubeA+cubeB+cubeC) and not(d in cubes):
                        print(f"{a}³\t+{b}³\t+{c}³\t={d}³")
                        cubes.append(d)
                        if len(cubes)==numberToGenerate:
                            return
maxSize = 50
cubesToGenerate=5
getCubes(maxSize, cubesToGenerate)