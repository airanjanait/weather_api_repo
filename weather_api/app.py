from flask import Flask,request,render_template
from function import weather
app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    weat=""
    if request.method=='POST':
        weat=""
        var=request.form.get("city")
        weat=""
        print(var)
        weat=weather(var)
    return render_template("home.html",weat=weat)



        
if __name__=="__main__":
    app.run(debug=True)
    