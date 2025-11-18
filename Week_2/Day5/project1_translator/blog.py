import json
from db import get_connection
from datetime import datetime
from translate import Translator
from gtts import gTTS
import os
import platform


class Blog:
    def __init__(self, title, content, blog_id=None, created_at=None, updated_at=None):
        self.id = blog_id
        self.title = title
        self.content = content
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()

    def save(self):
        try:
            connection = get_connection()
            if not connection:
                print("Could not establish database connection.")
                return False
            cursor = connection.cursor()
            insert_query = """
                INSERT INTO blogs (title, content)
                VALUES (%s, %s)
                RETURNING id, created_at, updated_at;
            """
            cursor.execute(insert_query, (self.title, self.content))
            result = cursor.fetchone()
            self.id = result[0]
            self.created_at = result[1]
            self.updated_at = result[2]
            connection.commit()
            cursor.close()
            print(f"✅ Blog saved with ID: {self.id}")
            return True
        except Exception as e:
            print(f"Error saving blog: {e}")
            if connection:
                connection.rollback()
            return False
        finally:
            if connection:
                connection.close()

    def update(self):
        if not self.id:
            print("Cannot update blog without ID")
            return False
            
        try:
            connection = get_connection()
            if not connection:
                print("Could not establish database connection.")
                return False
            cursor = connection.cursor()
            update_query = """
                UPDATE blogs
                SET title = %s,
                    content = %s,
                    updated_at = NOW()
                WHERE id = %s
                RETURNING updated_at;
            """
            cursor.execute(update_query, (self.title, self.content, self.id))
            result = cursor.fetchone()
            if result:
                self.updated_at = result[0]
            connection.commit()
            cursor.close()
            print(f"✅ Blog {self.id} updated successfully")
            return True
        except Exception as e:
            print(f"Error updating blog: {e}")
            if connection:
                connection.rollback()
            return False
        finally:
            if connection:
                connection.close()

    def delete(self):
        if not self.id:
            print("Cannot delete blog without ID")
            return False
            
        try:
            connection = get_connection()
            if not connection:
                print("Could not establish database connection.")
                return False
            cursor = connection.cursor()
            delete_query = """
                DELETE FROM blogs
                WHERE id = %s;
            """
            cursor.execute(delete_query, (self.id,))
            connection.commit()
            cursor.close()
            print(f"✅ Blog {self.id} deleted successfully")
            return True
        except Exception as e:
            print(f"Error deleting blog: {e}")
            if connection:
                connection.rollback()
            return False
        finally:
            if connection:
                connection.close()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": str(self.created_at) if self.created_at else None,
            "updated_at": str(self.updated_at) if self.updated_at else None
        }

    @staticmethod
    def get_all():
        connection = None
        try:
            connection = get_connection()
            if not connection:
                print("Could not establish database connection.")
                return []
            cursor = connection.cursor()
            select_query = """
                SELECT id, title, content, created_at, updated_at
                FROM blogs
                ORDER BY created_at DESC;
            """
            cursor.execute(select_query)
            rows = cursor.fetchall()
            blogs = []
            
            # Create Blog instances for each row
            for row in rows:
                blog = Blog(
                    title=row[1],
                    content=row[2],
                    blog_id=row[0],
                    created_at=row[3],
                    updated_at=row[4]
                )
                blogs.append(blog)
            
            return blogs
        except Exception as e:
            print(f"Error fetching blogs: {e}")
            return []
        finally:
            if connection:
                cursor.close()
                connection.close()

    @staticmethod
    def get_by_id(blog_id):
        connection = None
        try:
            connection = get_connection()
            if not connection:
                print("Could not establish database connection.")
                return None
            cursor = connection.cursor()
            select_query = """
                SELECT id, title, content, created_at, updated_at
                FROM blogs
                WHERE id = %s;
            """
            cursor.execute(select_query, (blog_id,))
            row = cursor.fetchone()
            
            if row:
                blog = Blog(
                    title=row[1],
                    content=row[2],
                    blog_id=row[0],
                    created_at=row[3],
                    updated_at=row[4]
                )
                return blog
            else:
                return None
        except Exception as e:
            print(f"Error fetching blog by id: {e}")
            return None
        finally:
            if connection:
                cursor.close()
                connection.close()

    def translate_and_speak(self, source_lang='fr', target_lang='en'):
        
        try:
            print(f"\n🔄 Translating blog: '{self.title}'...")
            print(f"Original content ({source_lang}):\n{self.content}\n")

            # Step 1: Translate the content
            translator = Translator(from_lang=source_lang, to_lang=target_lang)
            translated_text = translator.translate(self.content)

            print(f"✅ Translated content ({target_lang}):\n{translated_text}\n")

            # Step 2: Convert translated text to speech
            print("🔊 Converting to speech...")
            tts = gTTS(text=translated_text, lang=target_lang, slow=False)

            # Save audio file
            audio_file = f"blog_{getattr(self, 'id', 'new')}_audio.mp3"
            tts.save(audio_file)
            print(f"✅ Audio saved as: {audio_file}")

            # Step 3: Play the audio (optional)
            print("▶️  Playing audio...")
            self._play_audio(audio_file)

            return translated_text, audio_file

        except Exception as e:
            print(f"❌ Error in translate_and_speak: {e}")
            return None, None

    def _play_audio(self, audio_file):
      
        try:
            system = platform.system()

            if system == "Darwin":  # macOS
                os.system(f"afplay {audio_file}")
            elif system == "Linux":
                os.system(f"mpg123 {audio_file}")
            elif system == "Windows":
                os.system(f"start {audio_file}")
            else:
                print(f"⚠️ Auto-play not supported on {system}. Please play {audio_file} manually.")

            print("✅ Audio played successfully!")

        except Exception as e:
            print(f"❌ Error playing audio: {e}")
            print(f"Please play the file manually: {audio_file}")


# ============ TEST CODE (Only runs when script is executed directly) ============
if __name__ == "__main__":
    # Uncomment to test the Blog class
    print("Testing Blog class...")
    
    # Test 1: Create and save a blog
    # blog = Blog("Test Blog", "This is a test content.")
    # blog.save()
    
    # Test 2: Get all blogs
    # blogs = Blog.get_all()
    # print(f"\nTotal blogs: {len(blogs)}")
    # for blog in blogs:
    #     print(blog.to_dict())
    
    # Test 3: Get blog by ID
    # blog = Blog.get_by_id(1)
    # if blog:
    #     print(f"\nFetched blog: {blog.to_dict()}")
    
    # Test 4: Update a blog
    # blog = Blog.get_by_id(1)
    # if blog:
    #     blog.title = "Updated Title"
    #     blog.content = "Updated content"
    #     blog.update()
    
    # Test 5: Delete a blog
    # blog = Blog.get_by_id(2)
    # if blog:
    #     blog.delete()
    
    # Test 6: Translate and speak
    # blog = Blog("Bonjour", "Bonjour le monde, j'espère que vous allez bien.")
    # blog.save()
    # blog.translate_and_speak(source_lang="fr", target_lang="en")
    
    pass