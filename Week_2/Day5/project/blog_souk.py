import json
from sys import platform
from db import get_connection
from datetime import datetime
from translate import Translator
from gtts import gTTS
import os
import platform



class Blog:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):     #instance method because it works on instance (self)
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
            #self.updated_at = result[2]
            connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error saving blog: {e}")
            connection.rollback() 
            return False
        finally:
            if connection:
                connection.close()

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
            rows = cursor.fetchall() # this data is Array of arrays [[1, "bonjour", ..., ..., ...], [], []], we want array of the objects [{id: 1, title: "bonjour", ...}, {}, {}]
            blogs = []
            for row in rows:
                blog = { 
                    "id": row[0],
                    "title": row[1],
                    "content": row[2],
                    "created_at": row[3],
                    "updated_at": row[4]
                }

                # blog = Blog(row[1], row[2])
                # blog.id = row[0]
                # blog.created_at = row[3]
                # blog.updated_at = row[4]
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
        blog = None
        #connection = None
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
                blog = { 
                    "id": row[0],
                    "title": row[1],
                    "content": row[2],
                    "created_at": str(row[3]), #datatime to string because json cant handle datetime objects, it handles only str, int, float, bool
                    "updated_at": str(row[4])
                }
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
    @staticmethod
    def delete_by_id(blog_id):
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
            cursor.execute(delete_query, (blog_id,))
            print(f"Blog with id {blog_id} deleted.")
            connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error deleting blog by id: {e}")
            connection.rollback() 
            return False
        finally:
            if connection:
                connection.close()
    @staticmethod
    def update(blog_id, title, content):
        connection = None
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
                WHERE id = %s;
                """
            cursor.execute(update_query, (title, content, blog_id))
            connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error updating blog: {e}")
            connection.rollback() 
            return False
        finally:
            if connection:
                connection.close()
# if __name__ == "__main__":
#     # blog1= Blog("My First Blog", "This is the content of my first blog.")
#     # blog1.save()
#     # blog2= Blog("My Second Blog", "This is the content of my second blog.")
#     # blog2.save()
#     # print("Blogs saved successfully.")
#     # print(f"blog1 : {blog1.title}, {blog1.content}, {blog1.created_at}, {blog1.updated_at}")
#     # print(f"blog2 : {blog2.title}, {blog2.content}, {blog2.created_at}, {blog2.updated_at}")
#     #  blogs = Blog.get_all()
#     # # for blog in blogs:
#     # #     print(blog)
#     # print(blogs)
#     # print(Blog.get_by_id(1))
#     # print(json.dumps(Blog.get_by_id(1), indent=4))  
#     #print(Blog.delete_by_id(2))
#     print(json.dumps(Blog.update(1, "Updated Title", "Updated Content"), indent=4))

# def translate_and_speak(self, source_lang='fr', target_lang='en'):
#         """
#         Instance method: Translates blog content and converts it to speech.
        
#         This method demonstrates:
#         1. Using external libraries (translate, gTTS)
#         2. Working with files (saving audio)
#         3. Platform-specific code (playing audio)
        
#         Args:
#             source_lang (str): Source language code (default: 'fr' for French)
#             target_lang (str): Target language code (default: 'en' for English)
        
#         Returns:
#             str: Translated text, or None if error occurs
#         """
#         try:
#             print(f"\n🔄 Translating blog: '{self.title}'...")
#             print(f"Original content ({source_lang}):\n{self.content}\n")
            
#             # Step 1: Translate the content
#             translator = Translator(from_lang=source_lang, to_lang=target_lang)
#             translated_text = translator.translate(self.content)
            
#             print(f"✅ Translated content ({target_lang}):\n{translated_text}\n")
            
#             # Step 2: Convert translated text to speech
#             print("🔊 Converting to speech...")
#             tts = gTTS(text=translated_text, lang=target_lang, slow=False)
            
#             # Save audio file
#             audio_file = f"blog_{self.id}_audio.mp3"
#             tts.save(audio_file)
#             print(f"✅ Audio saved as: {audio_file}")
            
#             # Step 3: Play the audio (platform-specific)
#             print("▶️  Playing audio...")
#             self._play_audio(audio_file)
            
#             return translated_text
            
#         except Exception as e:
#             print(f"❌ Error in translate_and_speak: {e}")
#             return None
    
# def _play_audio(self, audio_file):
#         """
#         Private helper method: Plays audio file based on the operating system.
        
#         Args:
#             audio_file (str): Path to the audio file
#         """
#         try:
#             system = platform.system()
                
#             if system == "Darwin":  # macOS
#                 os.system(f"afplay {audio_file}")
#             elif system == "Linux":
#                 os.system(f"mpg123 {audio_file}")
#             elif system == "Windows":
#                 os.system(f"start {audio_file}")
#             else:
#                 print(f"⚠️  Auto-play not supported on {system}. Please play {audio_file} manually.")
                
#             print("✅ Audio played successfully!")
                
#         except Exception as e:
#             print(f"❌ Error playing audio: {e}")
#             print(f"Please play the file manually: {audio_file}")

    def translate_and_speak(self, source_lang='fr', target_lang='en'):
        """
        Instance method: Translates blog content and converts it to speech.
        """
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

            # Step 3: Play the audio
            print("▶️  Playing audio...")
            self._play_audio(audio_file)

            return translated_text

        except Exception as e:
            print(f"❌ Error in translate_and_speak: {e}")
            return None

    def _play_audio(self, audio_file):
        """
        Private helper method: Plays audio file based on the operating system.
        """
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



blog = Blog("Bonjour", "bonjour le monde, j'espere que vous allez bien.")
blog.save()
blog.translate_and_speak(source_lang="fr", target_lang="en")
