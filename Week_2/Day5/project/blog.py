import os
import psycopg2
from datetime import datetime
from db import get_connection   # import your helper function

   
class Blog:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    """"get_connection(): Opens access to the database; foundation for all operations.
    conn.cursor(): Executes queries and fetches results; you can’t run SQL without it.
    CREATE TABLE IF NOT EXISTS: Safe bootstrapping; your app self-prepares the storage.
    Parameterized VALUES (%s,...): Security and correctness; avoids injection and casting issues.
    RETURNING id: Immediate access to the new primary key; essential for follow-up operations.
    cursor.fetchone(): Retrieves data from the last command; here, it gives you the id.
    conn.commit(): Makes changes durable; without it, inserts can be lost.
    conn.rollback(): Keeps data clean on errors; ensures atomicity.
    close(): Frees connections/cursors; prevents resource exhaustion."""

    def save(self):
        conn = get_connection()
        if not conn:
            print("Could not establish database connection.")
            return        
        try:
            cursor = conn.cursor()
            # Create table if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS blogs (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    content TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT NOW(),
                    updated_at TIMESTAMP DEFAULT NOW()
                )
            """)            
            # Insert blog data
            cursor.execute("""
                INSERT INTO blogs (title, content, created_at, updated_at)
                VALUES (%s, %s, %s, %s)
                RETURNING id;
            """, (self.title, self.content, self.created_at, self.updated_at))            
            # Fetch the auto-generated id if not provided
            new_id = cursor.fetchone()[0]
            self.id = new_id            
            conn.commit()
            cursor.close()
            conn.close()
            print(f"Blog '{self.title}' saved successfully with id {self.id}!")
        
        except Exception as e:
            print("Error saving blog:", e)
            conn.rollback()
            conn.close()

def update(self):
    conn = get_connection()
    if not conn:
        print("Could not establish database connection.")
        return    
    try:
        cursor = conn.cursor()        
        # Update the blog record by id
        cursor.execute("""
            UPDATE blogs
            SET title = %s,
                content = %s,
                updated_at = %s
            WHERE id = %s;
        """, (self.title, self.content, datetime.now(), self.id))        
        # Check if any row was updated
        if cursor.rowcount == 0:
            print(f"No blog found with id {self.id}.")
        else:
            print(f"Blog with id {self.id} updated successfully!")        
        conn.commit()
        cursor.close()
        conn.close()    
    except Exception as e:
        print("Error updating blog:", e)
        conn.rollback()
        conn.close()
    def delete(self):
        conn = get_connection()
        if not conn:
            print("Could not establish database connection.")
            return        
        try:
            cursor = conn.cursor()            
            # Delete the blog record by id
            cursor.execute("""
                DELETE FROM blogs
                WHERE id = %s;
            """, (self.id,))            
            # Check if any row was deleted
            if cursor.rowcount == 0:
                print(f"No blog found with id {self.id}.")
            else:
                print(f"Blog with id {self.id} deleted successfully!")            
            conn.commit()
            cursor.close()
            conn.close()        
        except Exception as e:
            print("Error deleting blog:", e)
            conn.rollback()
            conn.close()

        @staticmethod
        def get_all():
            conn = get_connection()
            if not conn:
                print("Could not establish database connection.")
                return []            
            try:
                cursor = conn.cursor()                
                # Retrieve all blog records
                cursor.execute("""
                    SELECT id, title, content, created_at, updated_at
                    FROM blogs;
                """)                
                rows = cursor.fetchall()                
                blogs = []
                for row in rows:
                    blog = Blog(row[0], row[1], row[2])
                    blog.created_at = row[3]
                    blog.updated_at = row[4]
                    blogs.append(blog)                
                cursor.close()
                conn.close()                
                return blogs            
            except Exception as e:
                print("Error retrieving blogs:", e)
                conn.close()
                return []
            

    def translate_and_speak(self):
        translator = Translator()

        # Translate the text
        translated = translator.translate(self.text, dest=self.dest_lang)
        translated_text = translated.text
        print("Translated:", translated_text)

        # Convert to speech
        filename = f"audio_{uuid.uuid4().hex}.mp3"  # unique filename
        tts = gTTS(translated_text, lang=self.dest_lang)
        tts.save(filename)

        # Play the audio
        playsound(filename)

        # Optional: remove file after playing
        os.remove(filename)
        
    @staticmethod
    def get_by_id(blog_id):
        conn = get_connection()
        if not conn:
            print("Could not establish database connection.")
            return None        
        try:
            cursor = conn.cursor()            
            # Retrieve the blog record by id
            cursor.execute("""
                SELECT id, title, content, created_at, updated_at
                FROM blogs
                WHERE id = %s;
            """, (blog_id,))            
            row = cursor.fetchone()            
            cursor.close()
            conn.close()            
            if row:
                blog = Blog(row[0], row[1], row[2])
                blog.created_at = row[3]
                blog.updated_at = row[4]
                return blog
            else:
                print(f"No blog found with id {blog_id}.")
                return None        
        except Exception as e:
            print("Error retrieving blog:", e)
            conn.close()
            return None


blog2 = Blog(None, "Leila", "Flouuussss")
blog2.save()
