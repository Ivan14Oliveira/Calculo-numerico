def dec_hex(n):
  """
  Parametros
  n: número inteiro positivo
    Número decimal 
  """
  hex = ""
  while int(n) !=0:
    a = int(n%16)
    if a < 10:
      hex  += str(a)
    else: 
      hex += chr(55+a)
    n /= 16 
  return hex[::-1]

def main():
  a = int(input("Digite o seu número"))
  print(f"Seu número em hexadecimal é: {a}")
if __name__ == __main__:
  main()
