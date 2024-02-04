
"""
GreenMeet. server.py file
"""
import os
from flask import Flask, request, render_template, session, g, redirect, Response, abort, url_for, send_from_directory

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login/')
def login():
   return render_template('login.html')

@app.route('/loggingin', methods=['GET'])
def loggingin():
   
   admin_email = request.args.get('admin_email')
   if admin_email:
      # call to add admin email
      print("admin email")
      return render_template('admin.html')

   user_email = request.args.get('user_email')
   if user_email:
      # call to add user_email
      print("user email")
      return render_template('user.hmtl')
   
  
@app.route('/signingup', methods=['GET'])
admin_name = request.args.get('admin_name')
admin_email = request.args.get('admin_email')
admin_password = request.args.get('admin_password')

contributor_name = request.args.get('contributor_name')
contributor_email = request.args.get('contributor_email')
contributor_password = request.args.get('contributor_password')

   

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
