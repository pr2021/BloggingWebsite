from flask import render_template,request,Blueprint
from Post.models import BlogPost

core = Blueprint('core',__name__)

@core.route('/')
def index():
    '''
    This is the home page view. Notice how it uses pagination to show a limited
    number of posts by limiting its query size and then calling paginate.
    '''
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html',blog_posts=blog_posts)

@core.route('/info')
def info():
    '''
    Example view of any other "core" page. Such as a info page, about page,
    contact page. Any page that doesn't really sync with one of the models.
    '''
    return render_template('info.html')
from datetime import date

from flask import Blueprint, render_template
from flask_login import current_user
from flask_login import login_required

home = Blueprint('home', __name__, url_prefix='/home')


@home.route('/')
@login_required
def home_page():
    upcoming_bookings = list(filter(lambda x: x.booking_date == date.today(), current_user.booking_details))
    return render_template('home/home.html', upcoming_bookings=upcoming_bookings)
    
