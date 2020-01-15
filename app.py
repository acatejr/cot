from flask import Flask, jsonify
from flask import render_template
from flask_graphql import GraphQLView
from models import db_session
from schema import schema, Incident

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

incidents = [
    {
        'id': 1,
        'title': u'Incident 1 title',
        'description': u'Something bad happened!',
        'status': u'Resolved',
        'lat': 32.2239699,
        'lng': -110.9720529,
    },
    {
        'id': 2,
        'title': u'Incident 2 title',
        'description': u'Something sinister happened!',
        'status': u'Resolved',
        'lat': 32.247611,
        'lng': -110.9763407,
    },
    {
        'id': 3,
        'title': u'Incident 3 title',
        'description': u'Something unsavory happened!',
        'status': u'Resolved',
        'lat': 32.241017,
        'lng': -110.9859277,
    },
    {
        'id': 4,
        'title': u'Incident 4 title',
        'description': u'Something not cool happened!',
        'status': u'Resolved',
        'lat': 32.2200639,
        'lng': -110.9805092,
    },
    {
        'id': 5,
        'title': u'Incident 5 title',
        'description': u'Something questionable happened!',
        'status': u'Resolved',
        'lat': 32.2221757,
        'lng': -110.9894626,
    },
]

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

