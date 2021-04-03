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
    
@home.route('/heartbeat')
def heart_beat():
    return "It Works" 
    