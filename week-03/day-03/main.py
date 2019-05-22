from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import csv

# url = request.urlopen("http://interthing.org/dmls/species.html")
# html = url.read()

# htmlf = open('dongdong69\week-03\day-03\templates\movies.html','r',encoding="utf-8")
# html_doc=htmlf.read()

# soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())

app = Flask(__name__, static_url_path="/static")


    
csvr = open('dongdong69\week-03\day-03\\templates\products.csv', encoding="utf-8", mode="r")
information = {}
lines = csv.reader(csvr)

index, name, price, qty = 0, 1, 2, 3

print(lines)

for line in lines:
    line = line[0].split(';')
    information[line[name]] = {}
    information[line[name]]["price"] = line[price]
    information[line[name]]["qty"] = line[qty]

csvr.close()

del information["name"]
print(information)

@app.route('/')
def hello_world():
    return render_template('homePage.html')

@app.route('/index')
def hello_name():
    return render_template('index.html')

@app.route('/<movie_id>')
def movies(movie_id):
    txtr = open(f"dongdong69\week-03\day-03\\templates\{movie_id}.txt", 'r')
    title = txtr.readline()
    p1 = txtr.readline()
    p2 = txtr.readline()
    p3 = txtr.readline()
    imgurl = txtr.readline()
    return render_template('movies.html', title = title, p1 = p1, p2 = p2, p3 = p3, imgurl = imgurl)
    txtr.close()

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/result', methods=["post"])
def result():
    search_name = request.form.get('name')
    search_price = request.form.get('price')
    search_qty = request.form.get('qty')

    search_price = search_price.split('-')
    search_qty = search_qty.split('-')

    print(search_name)

    if len(search_price) > 1:
        search_price = [number for number in range(int(search_price[0]), int(search_price[1]) + 1)]
    elif not search_price[0]:
        search_price = [number for number in range(200)]

    
    if len(search_qty) > 1:
        search_qty = [number for number in range(int(search_qty[0]), int(search_qty[1]) + 1)]
    elif not search_qty[0]:
        search_qty = [number for number in range(20)]

    print(search_price)
    print(search_qty)

    results = []

    for names in information:
        if search_name in names and int(information[names]["price"]) in search_price and int(information[names]["qty"]) in search_qty:
            results.append("price:" + information[names]["price"] + ", qty:" + information[names]["qty"])

    if not results:
        return "Product not found"

    else:
        return render_template('result.html', result_list = results)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route("/doPost",methods=["post"])
def handPost():
    username = request.form.get('username1')
    password = request.form.get('password1')
    return "<h1>username:"+username+", password:"+password+"</h1>"

if __name__ == '__main__':
    app.run()