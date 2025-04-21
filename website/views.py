from flask import Blueprint, render_template,request, jsonify, send_file, send_from_directory, current_app

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/photo-booth')
def photobooth():
    return render_template("photo-booth.html")

@views.route('/more-info')
def moreinfo():
    return render_template("more-info.html")

@views.route('/support')
def support():
    return render_template("support.html")

@views.route('/requests')
def requests():
    return render_template("requests.html")

@views.route('/favicon.ico')
def favicon():
    return send_from_directory(current_app.static_folder, 'logo.png')

@views.route('/generate-qr', methods=['POST'])
def generate_qr():
    try:
        # Get the image data from the request
        data = request.get_json()
        if not data or 'image' not in data:
            return jsonify({'error': 'No image data provided'}), 400
            
        # Extract base64 image data (remove the data URL prefix if present)
        image_data = data['image']
        if image_data.startswith('data:image/png;base64,'):
            image_data = image_data.replace('data:image/png;base64,', '')
        
        # Decode the base64 image
        image_bytes = base64.b64decode(image_data)
        
        # Create a file-like object in memory
        image_file = io.BytesIO(image_bytes)
        
        # Return the image as a downloadable file
        return send_file(
            image_file,
            mimetype='image/png',
            as_attachment=True,
            download_name='picobooth-qr.png'
        )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500