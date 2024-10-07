from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.objectid import ObjectId
from pymongo.errors import CollectionInvalid
app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb+srv://aakritimehrotra2022:AAKRITI%408oct@cluster0.qmt1szv.mongodb.net/newDb" 
mongo = PyMongo(app)
CORS(app)


# Function to create collection with schema validation
def create_overlays_collection():
    db = mongo.db
    try:
        # Define the schema
        db.create_collection("overlays", validator={
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["position", "size", "content", "rtsp_url"],
                "properties": {
                    "position": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "size": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "content": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "rtsp_url": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    }
                }
            }
        })
        print("Overlays collection created with schema validation.")
    except CollectionInvalid:
        print("Collection already exists.")

# Call the function when the app starts

with app.app_context():
    create_overlays_collection()

# CRUD for overlay settings
@app.route('/overlays', methods=['POST'])

def create_overlay():
    data = request.json
    overlays_collection = mongo.db.overlays
    new_overlay = {
        'position': data.get('position'),
        'size': data.get('size'),
        'content': data.get('content'),
        'rtsp_url': data.get('rtsp_url')
    }
    overlays_collection.insert_one(new_overlay)
    return jsonify({'message': 'Overlay created successfully'}), 201

@app.route('/overlays', methods=['GET'])

def get_overlays():
    overlays_collection = mongo.db.overlays
    overlays = list(overlays_collection.find())
    for overlay in overlays:
        overlay['_id'] = str(overlay['_id'])  # Convert ObjectId to string
    return jsonify(overlays)

@app.route('/overlays/<id>', methods=['PUT'])

def update_overlay(id):
    data = request.json
    overlays_collection = mongo.db.overlays
    overlays_collection.update_one(
        {'_id': ObjectId(id)},
        {'$set': {
            'position': data.get('position'),
            'size': data.get('size'),
            'content': data.get('content'),
        }}
    )
    return jsonify({'message': 'Overlay updated successfully'})

@app.route('/overlays/<id>', methods=['DELETE'])

def delete_overlay(id):
    overlays_collection = mongo.db.overlays
    overlays_collection.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Overlay deleted successfully'})


@app.route('/stream', methods=['GET'])
def get_stream_url():
    
    return jsonify({'rtsp_url': 'https://rtsp.me/embed/rkEBEsYr/'})


if __name__ == '__main__':
    app.run(debug=True)
