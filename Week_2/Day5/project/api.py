from flask import Flask, request, jsonify
from blog import Blog
from dotenv import load_dotenv

app = Flask(__name__)

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
        if not data or 'title' not in data or 'content' not in data:
            return jsonify({"error": "Title and content are required"}), 400
        
        # Create and save blog using OOP
        blog = Blog(title=data['title'], content=data['content'])
        blog.save()
        
        return jsonify(blog.to_dict()), 201
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


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
        
        return jsonify(blogs_json), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/blogs/<int:blog_id>', methods=['GET'])
def get_blog(blog_id):
    """
    Get a single blog by ID.
    GET /blogs/<id>
    """
    try:
        blog = Blog.get_by_id(blog_id)
        
        if not blog:
            return jsonify({"error": "Blog not found"}), 404
        
        return jsonify(blog.to_dict()), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/blogs/<int:blog_id>', methods=['PUT'])
def update_blog(blog_id):
    """
    Update a blog.
    PUT /blogs/<id>
    Body: {"title": "...", "content": "..."}
    """
    try:
        data = request.get_json()
        
        # Fetch existing blog
        blog = Blog.get_by_id(blog_id)
        
        if not blog:
            return jsonify({"error": "Blog not found"}), 404
        
        # Update attributes
        if 'title' in data:
            blog.title = data['title']
        if 'content' in data:
            blog.content = data['content']
        
        # Save updates
        blog.update()
        
        return jsonify(blog.to_dict()), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/blogs/<int:blog_id>', methods=['DELETE'])
def delete_blog(blog_id):
    """
    Delete a blog.
    DELETE /blogs/<id>
    """
    try:
        blog = Blog.get_by_id(blog_id)
        
        if not blog:
            return jsonify({"error": "Blog not found"}), 404
        
        blog.delete()
        
        return jsonify({"message": f"Blog {blog_id} deleted successfully"}), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


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
            return jsonify({"error": "Blog not found"}), 404
        
        # Translate and generate audio
        translated_content, audio_file = blog.translate_and_speak(source_lang, target_lang)
        
        return jsonify({
            "id": blog.id,
            "original_title": blog.title,
            "original_content": blog.content,
            "translated_content": translated_content,
            "audio_file": audio_file
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ============ DEMONSTRATION OF FOR LOOPS, FILTER, MAP, LAMBDA ============

@app.route('/blogs/search', methods=['GET'])
def search_blogs():
    """
    Search blogs containing a keyword (demonstrates filter + lambda).
    GET /blogs/search?keyword=python
    """
    try:
        keyword = request.args.get('keyword', '').lower()
        
        # Get all blogs
        all_blogs = Blog.get_all()
        
        # Use filter and lambda to find matching blogs
        filtered_blogs = list(filter(
            lambda b: keyword in b.title.lower() or keyword in b.content.lower(),
            all_blogs
        ))
        
        # Use map and lambda to convert to dict
        result = list(map(lambda b: b.to_dict(), filtered_blogs))
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/blogs/stats', methods=['GET'])
def blog_stats():
    """
    Get statistics about blogs (demonstrates for loop).
    GET /blogs/stats
    """
    try:
        blogs = Blog.get_all()
        
        total_blogs = len(blogs)
        total_characters = 0
        
        # Use for loop to calculate statistics
        for blog in blogs:
            total_characters += len(blog.content)
        
        avg_length = total_characters // total_blogs if total_blogs > 0 else 0
        
        return jsonify({
            "total_blogs": total_blogs,
            "total_characters": total_characters,
            "average_content_length": avg_length
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ============ RUN SERVER ============

if __name__ == '__main__':
    app.run(debug=True, port=5000)



