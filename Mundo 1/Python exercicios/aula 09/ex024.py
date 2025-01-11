cidade = str(input('Em que cidade você nasceu: '))
cid = cidade.lower()
cid = cid.strip()
res = 'santo' in cid[:5]
print(cid)
print(res)