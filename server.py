
"""
GreenMeet. server.py file
"""
from main import check_admin_password_match, check_user_password_match, town_search, get_user_info, get_admin_info
import os
from flask import Flask, request, render_template, session, g, redirect, Response, abort, url_for, send_from_directory
from main import *

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/search')
def search():
   return render_template('search.html')

@app.route('/searchbar/', methods=['GET'])
def searchbar():
  searched = request.args.get('searched')
  valid_admins,valid_events = town_search(searched)
  return render_template('search.html', admins = valid_admins, events = valid_events)

@app.route('/login/')
def login():
   return render_template('login.html')

@app.route('/loggingin', methods=['GET'])
def loggingin():
   
   admin_email = request.args.get('admin_email')
   if admin_email:
      admin_password = request.args.get('admin_password')
      if check_admin_password_match(admin_email, admin_password):
        ADMINLOG = get_admin_info(admin_email)
        return render_template('admin.html', ADMINLOG = ADMINLOG)
      else :
        login_failed = True
        return render_template('login.html', login_failed=login_failed)
   

   user_email = request.args.get('user_email')
   if user_email:
      user_password = request.args.get('user_password')
      if check_user_password_match(user_email, user_password):
        USERLOG = get_user_info(user_email)
        return render_template('user.html', USERLOG = USERLOG)
      else :
        login_failed = True
        return render_template('login.html',login_failed=login_failed)
      # call to add user_email
      print("user email")
      return render_template('user.html')
   
  
@app.route('/signingup', methods=['GET'])

def signingup():
   admin_name = request.args.get('admin_name')
   admin_email = request.args.get('admin_email')
   admin_password = request.args.get('admin_password')

   if admin_email:
      add_admin(admin_email,admin_password,admin_name)
      return render_template('login.html')

   contributor_name = request.args.get('contributor_name')
   contributor_email = request.args.get('contributor_email')
   contributor_password = request.args.get('contributor_password')

   if contributor_email:
      add_user(contributor_email,contributor_password,contributor_name)
      return render_template('login.html')
   
@app.route('/signup/')
def signup():
   return render_template('signup.html')


#
# This is an example of a different path.  You can see it at:
#
#     localhost:8111/another
#
# Notice that the function name is another() rather than index()
# The functions for each app.route need to have different names
#

if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using:

        python3 server.py

    Show the help text using:

        python3 server.py --help

    """

    HOST, PORT = host, port
    print("running on %s:%d" % (HOST, PORT))
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)

  run()
