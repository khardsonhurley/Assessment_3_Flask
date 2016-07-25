from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

@app.route("/application-form")
def application():
    return render_template("application-form.html")

@app.route("/application")
def application_response():
    first_name = request.args.get("firstname")
    last_name = request.args.get("lastname")
    salary_input = request.args.get("salary")
    job_title = request.args.get("jobtitle")
    return render_template("application-response.html", firstname=first_name,
                                                        lastname=last_name, 
                                                        salary=salary_input,
                                                        job_title=job_title)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

