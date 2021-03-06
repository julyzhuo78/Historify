from flask import Flask
from flask import request, url_for, redirect, render_template
# from flask_api import FlaskAPI, status, exceptions
# import flask_login

# from gensim.summarization.summarizer import summarize

app = Flask(__name__)
app.secret_key = 'super secret string'

data = {
    0: {'ptName': 'patient\'s name',
        'cheifComplaint': 'chief complaint',
        'onset': 'onset',
        'quality': 'quality',
        'radiate': 'radiate',
        'severity': '',
        'dejavu': 'dejavu',
        'assoc': 'assoc',
        'aggrov': 'aggrov',
        'allev': 'allev',
        'function': '',
        'concern': '',
        'feel': '',
        'expect': '',
        'allergies': '',
        'surgeries': '',
        'illness': '',
        'hospital': '',
        'medication': '',
        'altTher': '',
        'momfhx': '',
        'dadfhx': '',
        'significant': '',
        'occupation': '',
        'underling': '',
        'livingSit': '',
        'smoke': '',
        'alcohol': '',
        'drugs': '',
        'sleep': '',
        'exercise': '',
        'diet': ''}
}

keys = ['ptName', 'cheifComplaint', 'onset', 'quality', 'radiate',
        'severity', 'dejavu', 'assoc', 'aggrov', 'allev', 'function',
        'concern', 'feel', 'expect', 'allergies', 'surgeries',
        'illness', 'hospital', 'medication', 'altTher', 'momfhx',
        'dadfhx', 'significant', 'occupation', 'underling',
        'livingSit', 'smoke', 'alcohol', 'drugs', 'sleep',
        'exercise', 'diet']

# mrns = {'Ada Lovelace': 0,
#        'Grace Hopper': 1,
#        'Katherine Johnson': 2}


def data_repr(key):
    return {
        'url': request.host_url.rstrip('/') + url_for('notes_detail', key=key),
        'data': data[key]
    }


@app.route("/", methods=['GET', 'POST'])
def data_list():
    """
    List or create notes.
    """
    if request.method == 'POST':
        # Only add data to existing patients
        # Assume that all patients are in the MRN database
        # TODO: read in POST object as a dictionary and iterate through to add values
        # for k, v in request.data.items():
        #     print(k, v)

        post_input = request.data

        for k, v in post_input.items():
            data[len(data.keys()) - 1][k] = v

    #     for k in keys:

    #     name = str(request.data.get('ptName', ''))

    #     
    #     name = post_input['ptName']
    #     # raw_text = str(request.data.get('text', ''))

    #     if name in mrns.values():
    #         mrn = mrns[name]

    #         observation_val = ['Chief complaint: {}'.format(post_input['cheifComplaint']),
    #                         'Onset: {}'.format(post_input['onset']),
    #                         'Quality: {}'.format(post_input['quality'])]

    #         # if data[mrn]['current_observation'] != '':
    #         #     data[mrn]['previous_observations'].append({'date': 'September 14, 2019',
    #         #         'observation': data[mrn]['current_observation']})
    #     else:
    #         raise exceptions.NotFound()

    #     # data[mrn]['current_observation'] = summarize(raw_text)

    #     # return data_repr(mrn), status.HTTP_201_CREATED

    # print('here')
    if request.method == 'GET':
        return render_template("Final_Hope.html", dict = data[0])

    return render_template("Final_Hope.html", dict = data[0])


@app.route("/<int:key>/", methods=['GET', 'PUT', 'DELETE'])
def notes_detail(key):
    """
    Retrieve, update or delete note instances.
    """
    if request.method == 'PUT':
        # note = str(request.data.get('text', ''))
        # notes[key] = note
        # return note_repr(key)
        raise exceptions.NotFound()

    elif request.method == 'DELETE':
        notes.pop(key, None)
        return '', status.HTTP_204_NO_CONTENT

    # request.method == 'GET'
    if key not in data:
        raise exceptions.NotFound()
    return data_repr(key)



if __name__ == "__main__":
    app.run(debug=True)
