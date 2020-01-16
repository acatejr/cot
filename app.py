from flask import Flask, jsonify
from flask import render_template
from flask_graphql import GraphQLView
from models import db_session
from schema import schema, Incident
from test_data import incidents

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api():
    pass

@app.route('/api/incidents')
def get_incidents():
    return jsonify({
        'incidents': incidents
    })

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
