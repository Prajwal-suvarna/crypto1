from flask import Flask, render_template, request

app = Flask(__name__)

mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

@app.route("/vernam", methods=["GET", "POST"])
def vernam():
    if request.method == "GET":
        return render_template("vernam.html")
    else:
        try:
            choice = int(request.form["choice"])
            key = request.form["key"].lower()

            if choice not in (1, 2):
                return render_template("Choose proper operations")
            if choice==1:
                plain=request.form["plain"]
                encrypt=[]
                for i in range(0,len(plain)):
                    if len(key)!=len(plain):
                        print(" ERROR !..length of key and plain should be same")
                        exit()
                    for k in range(0,len(mylist)):
                        if plain[i]==mylist[k]:
                            a1=k
                    for k in range(0,len(mylist)):
                        if key[i]==mylist[k] and i<=len(key):
                            a2=k
                    ans=a1^a2
                    ans1=ans%26
                    encrypt.append(mylist[ans1])
                return render_template("vernam.html",encrypted_text=encrypt,choice=choice)
            elif choice==2:
                cipher=request.form["cipher"]
                decrypt=[]
                for i in range(0,len(cipher)):
                    if len(key)!=len(cipher):
                        print("ERROR !...length of key and cipher should be same")
                        exit()
                    for k in range(0,len(mylist)):
                        if cipher[i]==mylist[k]:
                            a1=k
                    for k in range(0,len(mylist)):
                        if key[i]==mylist[k] and i<=len(key):
                            a2=k
                    ans=a1^a2
                    ans1=ans%26
                    decrypt.append(mylist[ans1])
                return render_template("vernam.html",decrypted_text=decrypt,choice=choice)
        except (ValueError, KeyError):
            return render_template("Invalid input or key format")

if __name__ == "__main__":
    app.run(debug=True, port=5500)
