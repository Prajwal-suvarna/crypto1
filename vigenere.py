from flask import Flask, render_template, request

app = Flask(__name__)

mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

@app.route("/vigenere", methods=["GET", "POST"])
def vigenere():
    if request.method == "GET":
        return render_template("vigenere.html")
    else:
        try:
            choice = int(request.form["choice"])
            key = request.form["key"].lower()

            if choice not in (1, 2):
                return render_template("Choose proper operations")

            if choice == 1:
                plain = request.form["plain"].lower()
                encrypt = []
                n = len(plain)
                j = 0
                for i in range(0, n):
                    if plain[i] == " ":
                        encrypt.append(plain[i])
                        continue
                    for k in range(0, len(mylist)):
                        if plain[i] == mylist[k]:
                            a1 = k
                    for k in range(0, len(mylist)):
                        if key[j % len(key)] == mylist[k]:
                            a2 = k
                    ans = a1 + a2
                    ans1 = ans % 26
                    encrypt.append(mylist[ans1])
                    j += 1
                return render_template("vigenere.html", encrypted_text=encrypt, choice=choice)

            elif choice == 2:  
                cipher = request.form["cipher"]
                cipher = cipher.lower()  
                decrypt = []
                j = 0
                for i in range(0, len(cipher)):
                    if cipher[i] == " ":
                        decrypt.append(cipher[i])
                        continue
                    for k in range(0, len(mylist)):
                        if cipher[i] == mylist[k]:
                            a1 = k
                    for k in range(0, len(mylist)):
                        if key[j % len(key)] == mylist[k]:
                            a2 = k
                    ans = a1 - a2
                    if ans < 0:
                        ans1 = ans + 26
                    else:
                        ans1 = ans % 26
                    decrypt.append(mylist[ans1])
                    j += 1
                return render_template("vigenere.html", decrypted_text=decrypt, choice=choice)

        except (ValueError, KeyError):
            return render_template("Invalid input or key format")

if __name__ == "__main__":
    app.run(debug=True, port=5500)
