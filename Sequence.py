i = int(input("เอากี่ชั้นดีคร๊าฟสุดหล่อ:"))
if i == 1:
    n = int(input("จะหาพจน์ที่เท่าไหร่ดีฮ๊าฟ: "))
    a_st = int(input("ใส่ค่าของพจน์ที่ 1 เลยฮ๊าฟ: "))
    d_st = int(input("ใส่ค่าของ d1 ชั้นที่ 1 ให้หน่อยฮ๊าฟ: "))
    an = int(a_st + (n - 1) * d_st)
    print(an)
elif i == 2:
    n = int(input("จะหาพจน์ที่เท่าไหร่ดีฮ๊าฟ: "))
    a_st = int(input("ใส่ค่าของพจน์ 1 เลยฮ๊าฟ: "))
    d_st = int(input("ใส่ค่าของ d1 ชั้นที่ 1 ให้หน่อยฮ๊าฟ: "))
    d_nd = int(input("ใส่ค่าของ d1 ชั้นที่ 2 ให้อีกนิดนึงฮ๊าฟ: "))
    an = int(a_st + (n - 1) * d_st + (((pow(n, 2) - (3 * n) + 2) * d_nd) / 2))
    print(an)
elif i == 3:
    n = int(input("จะหาพจน์ที่เท่าไหร่ดีฮ๊าฟ: "))
    a_st = int(input("ใส่ค่าของพจน์ 1 หน่อยฮ๊าฟ: "))
    d_st = int(input("ใส่ค่าของ d1 ชั้นที่ 1 ให้หน่อยฮ๊าฟ: "))
    d_nd = int(input("ใส่ค่าของ d1 ชั้นที่ 2 หน่อยฮ๊าฟ: "))
    d_rd = int(input("ใส่ค่าของ d1 ชั้นที่ 3 ให้อีกหน่อยนะฮ๊าฟ: "))
    an = int(a_st + (n - 1) * d_st + (((pow(n, 2) - (3 * n) + 2) * d_nd) / 2) + (((pow(n, 3) - (6 * pow(n, 2)) + (11 * n) - 6) * d_rd) / 6))
    print(an)
else:
    print("Sorry and fuck u!")