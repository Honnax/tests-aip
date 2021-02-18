school = {"1A": 21,"1Б": 17, "1В": 19, "1Г": 23}
a = int(input())
if a == 1:
    school[input("")] = input()
    print(school)
elif a == 2:
    addclass = {input(""): int(input())}
    school.update(addclass)
    print(school)
elif a == 3:
    del school[input("")]
    print(school)
elif a == 4:
    d=0
    for f in school:
        d+= school[f]
    print(d)
