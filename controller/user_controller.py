from app import app  #1st app is file name and 2nd app is variable name form app.py file

from flask import request,send_file
from datetime import datetime
import os, pathlib

from model.user_model import User_Model
obj = User_Model()

# CRUD Operations

# Read Operation
@app.route('/user/getall')
def user_getall_controller():
    return obj.user_getall_model()


# create operation
@app.route('/user/addone',methods=['POST'])
def user_addone_controller():
    return obj.user_addone_model(request.form)


# Update operation
@app.route('/user/update',methods=['PUT'])
def user_update_controller():
    return obj.user_update_model(request.form)

# Delete operation 
@app.route('/user/delete/<id>',methods=['Delete'])
def user_delete_controller(id):
    return obj.user_delete_model(id)


#Patch Operation 
@app.route('/user/patch/<id>',methods=['PATCH'])
def user_patch_controller(id):
    return obj.user_patch_model(request.form,id)



#pagination restapi enabled
@app.route('/user/getall/limit/<limit>/pageno/<page>',methods=['GET'])
def user_getall_controller_pagination(limit,page):
    return obj.user_getall_model_pagination(limit,page)


# uploading a file and saving it in particular folder and updating th db with filepath
@app.route('/user/<uid>/upload/avatar',methods=['put'])
def user_upload_avatar_controller(uid):
    file = request.files['avatar']

# creating unique name for the uploded_file using datetime module
    unique_file_name = str(datetime.now().timestamp()).replace('.','')

# Taking out filename and file extension separately
    file_name,extension = os.path.splitext(file.filename)

# Now concating the unique_file name with extension and giving path to store it in particular folder 
    final_file_name = f"uploads/{unique_file_name}{extension}"

# saving the file
    file.save(final_file_name)
    return obj.user_upload_avatar_model(uid,final_file_name)



# Displaying or reading the uploaded file using api 
@app.route('/uploads/<file_path>')
def user_display_avatar_controller(file_path):
    return send_file(f'uploads/{file_path}')


# JWT 