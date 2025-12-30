#made by bytoxicto

import random
import string
import zipfile
import os
nome_conta = input(("Nome da conta: ")).strip()
especiais = random.choices("!@#$%^&*()-_=+[]{}", k=4)
números = random.choices(string.digits, k=6)
letras = random.choices(string.ascii_letters, k=6)
senha = especiais + números + letras
random.shuffle(senha)
senha = "".join(senha)
nome_seguro = ''.join(c for c in nome_conta if c.isalnum() or c in (' ', '-', '_')).rstrip()
nome_arquivo_txt = f"{nome_seguro}.txt"
with open(nome_arquivo_txt, "w") as f:
    f.write(senha)
nome_zip = f"{nome_seguro}.zip"
with zipfile.ZipFile(nome_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(nome_arquivo_txt)
os.remove(nome_arquivo_txt)
print(f"\nSenha gerada para '{nome_conta}': {senha}")
print(f"Arquivo ZIP criado: {nome_zip}")
