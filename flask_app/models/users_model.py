from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = "users"

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# ----------- SAVE USER ------------------
    @classmethod
    def save(cls, data ):
        query = """
            INSERT INTO users ( first_name , last_name , email )
            VALUES ( %(first_name)s , %(last_name)s , %(email)s );
            """
        return connectToMySQL(DATABASE).query_db( query, data )
    

# ------------ GET ALL USERS ------------------
    @classmethod
    def get_all(cls):
        query = """
            SELECT * 
            FROM users;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

# ----------- GET ONE USER ------------------
    @classmethod
    def get_one(cls, id):
        data = {
            "id": id
        }
        query = """
            SELECT * 
            FROM users 
            WHERE id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

# ---------------- UPDATE ----------------
    @classmethod
    def edit_user(cls, data):
        query = """
            UPDATE users 
            SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s 
            WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    

# ----------------- DELETE ------------------
    @classmethod
    def delete(cls, id):
        query  = """
            DELETE FROM users
            WHERE id = %(id)s;
        """
        data = {"id": id}
        return connectToMySQL(DATABASE).query_db(query, data)
    
