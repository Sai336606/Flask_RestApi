import mysql.connector
import json
from flask import make_response

class User_Model:
    def __init__(self):
        # Connection establishment code
        try:
            self.con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="flask_db"
            )
            self.cur  = self.con.cursor(dictionary=True)
            print ("Connection established")
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL:")

        # commite code this will reflect in mysql server
        self.con.autocommit = True

# Read operation 
    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        results = self.cur.fetchall()
        # print(results)
        if len(results) < 1:
            return make_response({"message":"No users details found"},204)### 
        else:
            res = make_response({"payload":results},200) ###(using make response we are sending Response object it contains response body and https status code)  >>>>### this converts to json format<<<<
            # return results
            # return json.dumps(results) ###This  connverts any python object into JSON formated string  representation
            res.headers['Access-Control-Allow-Origin']='*'  ## CORS Access 
            return res

# Create operation
    def user_addone_model(self,data):
        try:
            self.cur.execute(f"insert into users (name,email,phone,role,password) values('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")

            return make_response({"message":"User Created successfully"},201)### 201 means created successfully it will  not return or display the output
        except Exception as e:
            return f"Error creating user: {str(e)}"

# Update operation
    def user_update_model(self,data):
        try:
            self.cur.execute(f"update users set name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' where id={data['id']}")

            if self.cur.rowcount > 0:
                return make_response({"message":"User updated successfully"},201)
            else:
                return make_response({"message":"User Not Found"},202)

        except Exception as e:
            return f"Error updating user: {str(e)}"

# Delete operation
    def user_delete_model(self,id):
        try:
            self.cur.execute(f"delete from users where id = {id}")
            if self.cur.rowcount > 0:
                return make_response({"message":"User Deleted successfully"},200)
            else:
                return make_response({"message":"User Not Found"},202)
        except Exception as e:
            return f"Error Deleting user: {str(e)}"


# Patch operation
    def user_patch_model(self,data,id):
        try:
            qur = "update users set"
            new_values = {}
            for key,value in data.items():
                new_values.update({key:value})
                qur = "update users set"
                values = ', '.join([f"{key}='{value}'" for key, value in data.items()])
                qur = qur + ' ' + values + f" where id={id}"
                self.cur.execute(qur)
                if self.cur.rowcount > 0:
                    return make_response({"message":"User Updated successfully"},200)
                else:
                    return make_response({"message":"User Not Found"},202)
        except Exception as e:
            return f"Error Deleting user: {str(e)}"
        
#Pagenation code 
    def user_getall_model_pagination(self,limit,page):
        limit = int(limit)
        page = int(page)
        start = (page*limit)-limit
        qur = f"select * from users limit {start},{limit}"
        self.cur.execute(qur)
        result = self.cur.fetchall()
        ## printing the output
        if len(result)<1:
            return make_response({"Message":"No users details found"},204)
        else:
            res = make_response({"payload":result,"Page_No:-":page,"limit":limit},200)
            res.headers['Access-Control-Allow-Origin']='*'
            return res
    
# Upload file and update the file_path in DB
    def user_upload_avatar_model(self,uid,filepath):
        try:
            self.cur.execute(f"update users set avatar = '{filepath}' where id = {uid}")
            if self.cur.rowcount >0 :
                 return make_response({"message":"User file_path successfully"},201)
            else:
                 return make_response({"message":"User Not Found"},202)
        except Exception as e:
            return f"Error updating user: {str(e)}"