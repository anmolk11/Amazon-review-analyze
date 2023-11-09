from flask import Flask,render_template,redirect,request
from main import Reviews

app = Flask(__name__)

def debug(*args):
    print('\n***************')
    print(args)
    print('***************\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reviews', methods=['POST','GET'])
def submit_url():
    if request.method == 'POST':
        website_url = request.form.get('websiteUrl')
        revs = Reviews(website_url)
        _review,_stars = revs.getReviews()
        # debug(len(data['review']))
        return render_template('review.html',review = _review,stars = _stars)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)

