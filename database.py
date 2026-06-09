from pymongo import MongoClient

client = MongoClient("mongodb+srv://Armando_Alvarez:Argbxb321404@hospital.lcpfmti.mongodb.net/?appName=HospitalE&retryWrites=true&w=majority")

db = client['HospitalE']