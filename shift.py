from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/shift", methods=["GET", "POST"])
def shift():
    if request.method=="GET":
        return render_template('shift.html')
    else:
        mylist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        choice=int(request.form["choice"])
        if choice==1:
            name=request.form["name"].lower()
            key=int(request.form["key"])
            name=name.lower()
            cipher=[]
            for k in range(0,len(name)):
                for j in range(0,len(mylist)):
                    if name[k]==" ":
                        continue
                    if name[k]==mylist[j]:
                        ans=(j+key)%26
                        cipher.append(mylist[ans])
            return render_template("shift.html",cipher=cipher,choice=choice)
        elif choice==2:
            cipher_txt=request.form["cipher_text"]
            key=int(request.form["key"])
            plain=[]
            for k in range(0,len(cipher_txt)):
                for j in range(0,len(mylist)):
                    if cipher_txt[k]==mylist[j]:
                        if j>=key:
                           ans=(j-key)%26
                           plain.append(mylist[ans])
                        else:
                           ans=((j-key)+26)%26
                           plain.append(mylist[ans])
            return render_template("shift.html",plain=plain,choice=choice)
        else:
            return render_template("Choose proper operation")
if __name__ == "__main__":
    app.run(debug=True,port=5500)
    
