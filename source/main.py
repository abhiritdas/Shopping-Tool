from flask import Flask, redirect, url_for, render_template, request
import scrape

app = Flask(__name__)

#default webapp page
@app.route("/")
def home():
    return "<h1>Hello!! Testing if it works on web!</h1>"

#opens search tab and sends POST request when something is typed
@app.route("/search", methods = ["POST", "GET"])
def search():
    if request.method == "POST":
        #receives "name" from search.html 
        search_attempt = request.form["name"]
        #redirects it to result function
        return redirect(url_for("result", result = search_attempt))
    else:    
        return render_template("search.html")


@app.route("/<result>")
def result(result):
    product_listings = []
    product_listings = scrape.scrape(result)
    return render_template("result.html", content = product_listings)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)