from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    language_John = ["Hello, John!", "你好约翰！", "سلام جان!", "こんにちはジョンさん！"]


    random_index = random.randint(0, len(language_John) - 1)
    return render_template('Random language.html', language = language_John[random_index])

@app.route('/products')
def products():
    products = [
    ("Milk", 3.59123),
    ("Bread", 2.96332),
    ("Rice", 0.64111)
    ]

    return render_template('products.html', products = products)

@app.route("/articles")
def list_articles():
    articles = [
    {
        "content": "Ne istas culpa ha im negat de. Ii perductae evertenda at desuescam. Nudi per ita sui dare ideo sola omne ordo. Sui sex item sane quum. Paucos sicuti tot qui tantae aliquo strata iis tantas. Mo purgantur at affirmans im reddendum co. Pleraque videntur ut ideamque imaginem ha.",
        "seen": ["John", "Jane", "Bob"]
    },
    {
        "content": "Aliud curam seu venti nihil sed istud volui eae qua. Autho ha falsi fidam tangi ut an tactu. Revera per eandem vox coelum videbo nam virtus. Item olim ei se duas ut. Ut mo ut peccato student adorare et diversa. Praecipuis ad conjunctam me percipitur agnoscerem at perfectius respondere. Horum meo porro uno debeo. Fallacem sentiens ha expertus delapsus dubitare ii. Ex ii efficiente et to perspicuae voluptatem arbitrabar.",
        "seen": ["John", "Jane"]
    },
    {
        "content": "Credendi at nequidem exhibere de. Debeo me dicam ex at ferri digna. Coloribus differant disputari vix cogitandi jam stabilire. Perfacile ut reliquiae perfectae ut. Fuisse falsas captum cui volent notior verbis sui. Meam idem nam ope prae isti quia jure hac. Lor durent has secius fronte usu auditu sumpti. Falso nomen aliud vim calor jam alias annos ubi. Movendi sum creatus vim fas majorem attendo propter. Sui videamus uno profecto refutent rom notitiam innumera potuerit.",
        "seen": ["John"]
    },
    {
        "content": "Potui habeo visus ens mea. An vi re continetur me familiarem negationem. Rei inveniri jam viderunt subducam tam imponere jam. Sub cui more ipsi meum.",
        "seen": []
    }
    ]
    return render_template("articles.html", articles=articles)

authors = [
    {
        "id": 100,
        "name": "John",
        "likes": [
            202,
            200
        ]
    },
    {
        "id": 101,
        "name": "jane",
        "likes" : [
            200
        ]
    }
]

posts = [
    {
        "id": 200,
        "author": 100,
        "content": "Difficulty on insensible reasonable in. From as went he they."
    },
    {
        "id": 201,
        "author": 100,
        "content": "Preference themselves me as thoroughly partiality considered on in estimating."
    },
    {
        "id": 202,
        "author": 101,
        "content": "In as name to here them deny wise this. As rapid woody my he me which."
    }
]

@app.route("/posts")
def list_posts():
    transformed_posts = None


    for author in authors:
        for post in posts:
            if author["id"] == post["author"]:
                post["name"] = author["name"]
            if post["id"] in author["likes"]:
                if "liked" not in post:
                    post["liked"] = []
                post["liked"].append(author["name"])

    transformed_posts = posts
    print(transformed_posts)

    return render_template("posts.html", posts=transformed_posts)

@app.route("/navigation")
def navigation():
    link_list = [('random', 'http://127.0.0.1:5000/'), ('product', 'http://127.0.0.1:5000/products'), ('article', 'http://127.0.0.1:5000/articles'), ('post', 'http://127.0.0.1:5000/posts')]
    return render_template("navigation.html", links=link_list)


if __name__ == "__main__":
    app.run()