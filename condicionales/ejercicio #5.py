monto = float(input("ingrese el monto total de su compra"))

if monto>=100:
    descuento= monto*(10/100)
    total = monto -descuento
    print("total de la cuenta", total)
if monto>=200:
    descuento= monto*(20/200)
    total = monto -descuento
    print("total de la cuenta", total)
   