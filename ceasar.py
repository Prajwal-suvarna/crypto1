from flask import Flask, render_template, request

app = Flask(__name__)

mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

@app.route("/ceasar", methods=["GET", "POST"])
def ceasar():
    if request.method == "GET":
        return render_template("ceasar.html")
    else:
        choice = int(request.form["choice"])
        name = request.form["name"].lower()
        cipher = []
        plain = []

        if choice == 1:
            for k in range(0, len(name)):
                for j in range(0, len(mylist)):
                    if name[k] == " ":
                        continue
                    if name[k] == mylist[j]:
                        ans = (j + 3) % 26
                        cipher.append(mylist[ans])
            return render_template("ceasar.html", cipher=cipher, choice=choice)

        elif choice == 2:
            for k in range(0, len(request.form["cipher_txt"])):
                for j in range(0, len(mylist)):
                    if request.form["cipher_txt"][k] == mylist[j]:
                        if j >= 3:
                            ans = (j - 3) % 26
                        else:
                            ans = ((j - 3) + 26) % 26
                        plain.append(mylist[ans])
            return render_template("ceasar.html", plain=plain, choice=choice)

        else:
            return render_template("ceasar.html", error="Choose correct option")

if __name__ == "__main__":
    app.run(debug=True,port=5500)

