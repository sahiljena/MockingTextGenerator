from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/swag-text/',methods = ["POST","GET"])
def swag_text():
    text=request.args.get("text")
    if text:
        text=request.args.get("text")
        d = text.split()
        f = ""
        buffer_text = ""
        if not text:
            text="Invalid Input!"
        else:
            for i in range(len(d)):
	            for j in range(len(d[i])):
		            if j%2 == 0:
			            buffer_text += (d[i])[j].upper()
		            else:
			            buffer_text += (d[i])[j].lower()
	            d[i] = buffer_text
	            buffer_text = ""
            for i in d:
                f += i+" "
            return render_template('swag-text.html',text = f, got = text)
            
    return render_template('swag-text.html')

