from pyscript import document, display



def receipt(e):
    latte = document.getElementById("350")
    espresso = document.getElementById("300")
    mocha = document.getElementById("250")
    hot_chocolate = document.getElementById("550")
    iced_coffee= document.getElementById("50")

    vat = (float(latte.value) * latte.checked + float(espresso.value) * espresso.checked float(mocha.value) * mocha.checked float(hot_chocolate.value) * hot_chocolate.checked float(iced_coffee.value) * iced_coffee.checked)

    total_amount = vat * 0.12

display(f'Total Amount : {total_amount}, ')


