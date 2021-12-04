alfavit_zifri = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
zbilshenya = int(input('На скільки збільшити: '))
message = input("Повідомлення: ")
widpovid = ''
for a in message:
    old_bukva = alfavit_zifri.find(a)
    new_bukva = old_bukva + zbilshenya
    if a in alfavit_zifri:
        widpovid += alfavit_zifri[new_bukva]
    else:
        widpovid += a
print (widpovid)
