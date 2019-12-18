from flask import render_template, request, Blueprint, current_app
from flaskblog.models import Post
from flask_googlemaps import Map, GoogleMaps

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    # When we add posts=posts, it creates the variable posts that we can utilize in the template
    page = request.args.get('page', default=1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts, title='Home')

@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/map')
def map():
    mymap = Map(
                identifier="view-side",
                varname="mymap",
                lat=37.4419, # hardcoded!
                lng=-122.1419, # hardcoded!
                zoom=15,
                markers=[(37.4419, -122.1419)] # hardcoded!

            )

    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 37.4419,
             'lng': -122.1419,
             'infobox': "<b>Hello World</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 37.4300,
             'lng': -122.1400,
             'infobox': "<b>Hello World from other place</b>"
          }
        ]
    )
    return render_template('map.html', mymap=mymap, sndmap=sndmap, api_key=current_app.config['GMAPS_KEY'])