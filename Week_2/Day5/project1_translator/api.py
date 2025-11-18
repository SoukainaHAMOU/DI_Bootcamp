from flask import Flask, request, jsonify
from flask_cors import CORS
from blog import Blog
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# ============ CRUD ENDPOINTS ============

@app.route('/blogs', methods=['POST'])
def create_blog():
    """
    Create a new blog.
    POST /blogs
    Body: {"title": "...", "content": "..."}
    """
    try:
        data = request.get_json()
        
        # Validate input
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        if 'title' not in data or 'content' not in data:
            return jsonify({"error": "Title and content are required"}), 400
        
        # Validate that title and content are not empty
        if not data['title'].strip() or not data['content'].strip():
            return jsonify({"error": "Title and content cannot be empty"}), 400
        
        # Create and save blog using OOP
        blog = Blog(title=data['title'], content=data['content'])
        blog.save()
        
        return jsonify({
            "message": "Blog created successfully",
            "blog": blog.to_dict()
        }), 201
        
    except AttributeError as e:
        return jsonify({"error": f"Blog class method error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500


@app.route('/blogs', methods=['GET'])
def get_all_blogs():
    """
    Get all blogs.
    GET /blogs
    """
    try:
        # Fetch all blogs using static method
        blogs = Blog.get_all()
        
        # Use map and lambda to convert to dictionaries
        blogs_json = list(map(lambda b: b.to_dict(), blogs))
        
        return jsonify({
            "count": len(blogs_json),
            "blogs": blogs_json
        }), 200
        
    except AttributeError as e:
        return jsonify({"error": f"Blog class method error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500


@app.route('/blogs/<int:blog_id>', methods=['GET'])
def get_blog(blog_id):
    """
    Get a single blog by ID.
    GET /blogs/<id>
    """
    try:
        blog = Blog.get_by_id(blog_id)
        
        if not blog:
            return jsonify({"error": f"Blog with ID {blog_id} not found"}), 404
        
        return jsonify(blog.to_dict()), 200
        
    except AttributeError as e:
        return jsonify({"error": f"Blog class method error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500


@app.route('/blogs/<int:blog_id>', methods=['PUT'])
def update_blog(blog_id):
    """
    Update a blog.
    PUT /blogs/<id>
    Body: {"title": "...", "content": "..."}
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Fetch existing blog
        blog = Blog.get_by_id(blog_id)
        
        if not blog:
            return jsonify({"error": f"Blog with ID {blog_id} not found"}), 404
        
        # Update attributes
        if 'title' in data:
            if not data['title'].strip():
                return jsonify({"error": "Title cannot be empty"}), 400
            blog.title = data['title']
            
        if 'content' in data:
            if not data['content'].strip():
                return jsonify({"error": "Content cannot be empty"}), 400
            blog.content = data['content']
        
        # Save updates
        blog.update()
        
        return jsonify({
            "message": "Blog updated successfully",
            "blog": blog.to_dict()
        }), 200
        
    except AttributeError as e:
        return jsonify({"error": f"Blog class method error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500


@app.route('/blogs/<int:blog_id>', methods=['DELETE'])
def delete_blog(blog_id):
    """
    Delete a blog.
    DELETE /blogs/<id>
    """
    try:
        blog = Blog.get_by_id(blog_id)
        
        if not blog:
            return jsonify({"error": f"Blog with ID {blog_id} not found"}), 404
        
        blog.delete()
        
        return jsonify({
            "message": f"Blog {blog_id} deleted successfully"
        }), 200
        
    except AttributeError as e:
        return jsonify({"error": f"Blog class method error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500


# ============ TRANSLATION ENDPOINT ============

@app.route('/blogs/<int:blog_id>/translate', methods=['GET'])
def translate_blog(blog_id):
    """
    Translate blog content and generate audio.
    GET /blogs/<id>/translate?source=fr&target=en
    """
    try:
        # Get query parameters
        source_lang = request.args.get('source', 'en')
        target_lang = request.args.get('target', 'es')
        
        # Fetch blog
        blog = Blog.get_by_id(blog_id)
        
        if not blog:
            return jsonify({"error": f"Blog with ID {blog_id} not found"}), 404
        
        # Translate and generate audio
        translated_content, audio_file = blog.translate_and_speak(source_lang, target_lang)
        
        return jsonify({
            "id": blog.id,
            "original_title": blog.title,
            "original_content": blog.content,
            "translated_content": translated_content,
            "source_language": source_lang,
            "target_language": target_lang,
            "audio_file": audio_file
        }), 200
        
    except AttributeError as e:
        return jsonify({"error": f"Translation method error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500


# ============ RUN SERVER ============

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    app.run(debug=debug, port=port, host='0.0.0.0')