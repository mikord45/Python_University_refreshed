tab = [a * 2 for a in range(10)]
print(tab)

tab2 = [(a,b) for a in (1, 2, 3) for b in (1, 2)]
print(tab2)

tab3 = ["super" + x for x in ["-man", "-test"]]
print(tab3)

tab4 = [(a,b) for a in range(1,10) if a > 2 for b in range(1,10) if a % b == 0 and a != b and b != 1]
print(tab4)

tab5 = [(a,b) for a in range(1,10) if a > 2 for b in range(1,10) if a % b == 0 if a != b if b != 1]
print(tab5)

tab6 = [x for x in range(100) if 1024 in [x ** k for k in range(1,11)]]
print(tab6)