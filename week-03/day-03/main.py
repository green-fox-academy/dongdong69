from flask import Flask, request, render_template, jsonify, make_response
from bs4 import BeautifulSoup
import csv, json

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

for line in lines:
    line = line[0].split(';')
    information[line[name]] = {}
    information[line[name]]["price"] = line[price]
    information[line[name]]["qty"] = line[qty]

csvr.close()

del information["name"]

@app.route('/')
def hello_world():
    return render_template('homePage.html')

@app.route('/api/movies', methods=["POST", "GET", "PUT", "DELETE"])
def apiMovie():

    if request.method == 'POST':
        print("POST!!!!!!!!!!!!!!!!")
        headers = request.headers
        key = headers.get("X-Api-Key")
        print(key)

        if key == "dongdong":
            with open('dongdong69\week-03\day-03\\templates\movies.json', mode = 'r') as jsonr:
                information_movies = json.loads(jsonr.read())

            id_number = len(information_movies) + 1

            response = request.get_data()
            j_data =  json.loads(response)
            j_data["id"] = id_number
            information_movies.append(j_data)

            with open('dongdong69\week-03\day-03\\templates\movies.json', mode = 'w') as jsonw:
                json.dump(information_movies, jsonw)

            return jsonify(j_data)
        else:
            return jsonify({"error": "EInvalid API_KEY"}), 403


    if request.method == 'GET':
        with open('dongdong69\week-03\day-03\\templates\movies.json', mode = 'r') as jsonr:
            response = json.loads(jsonr.read())

        #response = make_response("not found", 404)

        response = jsonify(response)
        return response

    if request.method == 'PUT':

        headers = request.headers
        key = headers.get("X-Api-Key")

        if key == "dongdong":
            with open('dongdong69\week-03\day-03\\templates\movies.json', mode = 'r') as jsonr:
                information_movies = json.loads(jsonr.read())
                response = request.get_data()
                j_data =  json.loads(response)
                movie_id = j_data["id"]
                found = False
                for movie in information_movies:
                    if movie['id'] == movie_id:
                        found = True
                        movie['title'] = j_data['title']
                        movie['year'] = j_data['year']
                        movie['genre'] = j_data['genre']
                        movie['description'] = j_data['description']
            
            if not found:
                return jsonify({"error": f"No movie found with {movie_id} ID"}), 404

            else:
                with open('dongdong69\week-03\day-03\\templates\movies.json', mode = 'w') as jsonw:
                    json.dump(information_movies, jsonw)

                return jsonify({"success": f"You have already changed the movie {movie_id}"})

        else:
            return jsonify({"error": "EInvalid API_KEY"}), 403


    if request.method == 'DELETE':
        headers = request.headers
        key = headers.get("X-Api-Key")
        if key == "dongdong":
            with open('dongdong69\week-03\day-03\\templates\movies.json', mode = 'r') as jsonr:
                information_movies = json.loads(jsonr.read())
                response = request.get_data()
                j_data =  json.loads(response)
                movie_id = j_data["id"]
                found = False
                for movie in information_movies:
                    if movie['id'] == movie_id:
                        found = True
                        break
            if found:
                information_movies.remove(movie)
                with open('dongdong69\week-03\day-03\\templates\movies.json', mode = 'w') as jsonw:
                    json.dump(information_movies, jsonw)

                return jsonify({"success": f"You have already deleted the movie {movie_id}"})

            else:
                return jsonify({"error": f"No movie found with {movie_id} ID"}), 404


        else:
            return jsonify({"error": "EInvalid API_KEY"}), 403
            



@app.route('/api/movies/<movie_id>')
def apiMovieId(movie_id):
    #open and read the json file

    with open('dongdong69\week-03\day-03\\templates\movies.json', mode = 'r') as jsonr:
        response = json.loads(jsonr.read())[int(movie_id) - 1]

    #response = make_response("not found", 404)

    response = jsonify(response)
    return response

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

@app.route('/movies')
def movie():
    with open('dongdong69\week-03\day-03\\templates\movies.json', mode = 'r') as jsonr:
        information_movies = json.loads(jsonr.read())

    title_list = []
    for movie in information_movies:
        title_list.append(movie["title"])
    
    return render_template('movie_title.html', title_list = title_list)

@app.route('/edit-movie/<movie_id>', methods = ["GET"])
def edit_movie(movie_id):
    movie_id = int(movie_id)
    with open('dongdong69\week-03\day-03\\templates\movies.json', mode = 'r') as jsonr:
        information_movies = json.loads(jsonr.read())

    movie = information_movies[movie_id - 1]
    print(movie)
    return render_template('movie_edit.html', movie = movie)
    

if __name__ == '__main__':
    app.run()