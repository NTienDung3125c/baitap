so = float(input("so "))
hang_chuc = so // 10
hang_don_vi = so % 10
tong = hang_chuc + hang_don_vi
print(tong)


neu dung if

  so = float(input("so "))
if 10 <= so <= 99:
    hang_chuc = so // 10
    hang_don_vi = so % 10
    tong = hang_chuc + hang_don_vi
    print(tong)
else:
    print("failed")
