from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://api.npoint.io/9591ea8697a8b638a9a3"
    response = requests.get(url=url)
    all_posts = response.json()
    return render_template("index.html",posts=all_posts)

@app.route('/post/<blog_id>')
def find_blog(blog_id):
    url= "https://api.npoint.io/5714225b72aa9d113459"
    response = requests.get(url=url).json()
    return render_template('post.html', all_posts=response,blog=int(blog_id))
if __name__ == "__main__":
    app.run(debug=True)
