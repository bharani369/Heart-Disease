from flask import Flask, render_template, flash, request, session
import os
from flask import render_template, redirect, url_for, request
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from werkzeug.utils import secure_filename
import mysql.connector
import smtplib
#from PIL import Image
import pickle

import numpy as np

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import joblib



app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

app.config['DEBUG']


@app.route("/")
def homepage():
    return render_template('index.html')
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/Home")
def Home():
    return render_template('index.html')
@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')
@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')
@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')
@app.route("/UserHome")
def UserHome():
    return render_template('UserHome.html')
@app.route("/AdminHome")
def AdminHome():
    return render_template('AdminHome.html')

@app.route("/NewQuery1")
def NewQuery1():
    return render_template('NewQueryReg.html')

@app.route("/UploadDataset")
def UploadDataset():
    return render_template('ViewExcel.html')






@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'GET':
        return redirect('/AdminLogin')
    
    if request.method == 'POST':
       try:
           if request.form['uname'] == 'admin' or request.form['password'] == 'admin':
               conn = mysql.connector.connect(user=os.environ.get('DB_USER', 'root'), password=os.environ.get('DB_PASS', ''), host=os.environ.get('DB_HOST', 'localhost'), port=int(os.environ.get('DB_PORT', 26205)), connection_timeout=5, database=os.environ.get('DB_NAME', '1heartdb'), use_pure=True, charset='utf8')
               cursor = conn.cursor()
               cur = conn.cursor()
               cur.execute("SELECT * FROM register")
               data = cur.fetchall()
               return render_template('AdminHome.html', data=data)
    
           else:
               return """
               <!DOCTYPE html>
               <html>
               <head><title>Access Denied</title></head>
               <body style="text-align: center; font-family: sans-serif; padding-top: 100px; background: #f3f4f6;">
                   <script>alert('only admin login only allowed !');</script>
                   <h2 style="color: #ef4444;">Access Denied</h2>
                   <p>only admin login only allowed ! Please verify your credentials and try again.</p>
                   <a href="/AdminLogin" style="display: inline-block; padding: 10px 20px; background: #4f46e5; color: white; text-decoration: none; border-radius: 5px; margin-top: 20px;">Return to Admin Portal</a>
               </body>
               </html>
               """
       except Exception as e:
           import traceback
           return f"<h2>Backend Error</h2><pre>{str(e)}<br><br>{traceback.format_exc()}</pre>"

@app.route("/reg", methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        n = request.form['name']

        address = request.form['address']
        age = request.form['age']
        pnumber = request.form['phone']
        email = request.form['email']
        zip = request.form['zip']
        uname = request.form['uname']
        password = request.form['psw']
        conn = mysql.connector.connect(user=os.environ.get('DB_USER', 'root'), password=os.environ.get('DB_PASS', ''), host=os.environ.get('DB_HOST', 'localhost'), port=int(os.environ.get('DB_PORT', 26205)), connection_timeout=5, database=os.environ.get('DB_NAME', '1heartdb'), use_pure=True, charset='utf8')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO register VALUES ('','" + n + "','" + age + "','" + email + "','" + pnumber + "','" + zip + "','" + address + "','" + uname + "','" + password + "')")
        conn.commit()
        conn.close()
        return """
        <!DOCTYPE html>
        <html>
        <head><title>Registration Successful</title></head>
        <body style="background: #f3f4f6;">
            <script>
                alert('Welcome to HeartPredict! Please login to continue.');
                window.location.href = '/UserLogin';
            </script>
        </body>
        </html>
        """
@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    error = None
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user=os.environ.get('DB_USER', 'root'), password=os.environ.get('DB_PASS', ''), host=os.environ.get('DB_HOST', 'localhost'), port=int(os.environ.get('DB_PORT', 26205)), connection_timeout=5, database=os.environ.get('DB_NAME', '1heartdb'), use_pure=True, charset='utf8')
        cursor = conn.cursor()
        cursor.execute("SELECT * from register where uname='" + username + "' and psw='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            return render_template('index.html')
            return 'Username or Password is wrong'
        else:
            print(data[0])
            session['uid'] = data[0]
            conn = mysql.connector.connect(user=os.environ.get('DB_USER', 'root'), password=os.environ.get('DB_PASS', ''), host=os.environ.get('DB_HOST', 'localhost'), port=int(os.environ.get('DB_PORT', 26205)), connection_timeout=5, database=os.environ.get('DB_NAME', '1heartdb'), use_pure=True, charset='utf8')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM register where uname='" + username + "' and psw='" + password + "'")
            data = cur.fetchall()

            return render_template('UserHome.html', data=data )

@app.route("/newquery", methods=['GET', 'POST'])
def newquery():
    if request.method == 'POST':

        uname = session['uname']

        # Load model + columns
        model = joblib.load('heart_model.pkl')
        columns = joblib.load('columns.pkl')

        # 🔥 KEEP ORIGINAL VALUES (NO MANUAL ENCODING)
        features = {
            'Age': int(request.form['Age']),
            'Sex': request.form['Sex'],
            'ChestPainType': request.form['ChestPainType'],
            'RestingBP': int(request.form['RestingBP']),
            'Cholesterol': int(request.form['Cholesterol']),
            'FastingBS': int(request.form['FastingBS']),
            'RestingECG': request.form['RestingECG'],
            'MaxHR': int(request.form['MaxHR']),
            'ExerciseAngina': request.form['ExerciseAngina'],
            'Oldpeak': float(request.form['Oldpeak']),
            'ST_Slope': request.form['ST_Slope'],
            'HeartMRI': int(request.form['HeartMRI']),
            'CTScan': int(request.form['CTScan']),
            'Echocardiogram': int(request.form['Echocardiogram']),
            'ChestXray': int(request.form['ChestXray']),
            'Smoking': request.form['Smoking'],
            'Troponin': float(request.form['Troponin']),
            'Angio_Blockage_Percent': float(request.form['Angio_Blockage_Percent'])
        }

        # 🔥 Convert to DataFrame
        input_df = pd.DataFrame([features])

        # 🔥 SAME encoding as training
        input_df = pd.get_dummies(input_df)

        # 🔥 Align columns
        input_df = input_df.reindex(columns=columns, fill_value=0)

        # 🔥 Prediction
        prediction = model.predict(input_df)[0]
        prob = model.predict_proba(input_df)[0][1]

        # 🔥 Risk based on probability (BEST)
        if prob > 0.75:
            risk_level = " High Risk"
        elif prob > 0.45:
            risk_level = " Moderate Risk"
        else:
            risk_level = " Low Risk"

        print("Prediction:", prediction)
        print("Probability:", prob)

        # ✅ Store in DB (same as before)
        try:
            conn = mysql.connector.connect(user=os.environ.get('DB_USER', 'root'), password=os.environ.get('DB_PASS', ''), host=os.environ.get('DB_HOST', 'localhost'), port=int(os.environ.get('DB_PORT', 26205)), connection_timeout=5, database=os.environ.get('DB_NAME', '1heartdb'), use_pure=True, charset='utf8')
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO Querytb1 
                (UserName, Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG,
                MaxHR, ExerciseAngina, Oldpeak, ST_Slope, HeartMRI, CTScan, Echocardiogram, ChestXray,
                Smoking, Troponin, Angio_Blockage_Percent, Answer, Prescription)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                uname,
                features['Age'],
                features['Sex'],
                features['ChestPainType'],
                features['RestingBP'],
                features['Cholesterol'],
                features['FastingBS'],
                features['RestingECG'],
                features['MaxHR'],
                features['ExerciseAngina'],
                features['Oldpeak'],
                features['ST_Slope'],
                features['HeartMRI'],
                features['CTScan'],
                features['Echocardiogram'],
                features['ChestXray'],
                features['Smoking'],
                features['Troponin'],
                features['Angio_Blockage_Percent'],
                risk_level,
                'Consult Cardiologist Immediately' if prediction == 1 else 'Normal Checkup'
            ))

            conn.commit()
            conn.close()

        except Exception as e:
            print("Database Insert Error:", e)

        # Fetch user data
        conn = mysql.connector.connect(user=os.environ.get('DB_USER', 'root'), password=os.environ.get('DB_PASS', ''), host=os.environ.get('DB_HOST', 'localhost'), port=int(os.environ.get('DB_PORT', 26205)), connection_timeout=5, database=os.environ.get('DB_NAME', '1heartdb'), use_pure=True, charset='utf8')
        cur = conn.cursor()
        cur.execute("SELECT * FROM Querytb1 WHERE UserName=%s", (uname,))
        data = cur.fetchall()

        return render_template('UserQueryInfo.html', data=data)
@app.route("/UQueryandAns")
def UQueryandAns():

    uname = session['uname']

    conn = mysql.connector.connect(user=os.environ.get('DB_USER', 'root'), password=os.environ.get('DB_PASS', ''), host=os.environ.get('DB_HOST', 'localhost'), port=int(os.environ.get('DB_PORT', 26205)), connection_timeout=5, database=os.environ.get('DB_NAME', '1heartdb'), use_pure=True, charset='utf8')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Querytb1 where UserName='" + uname + "'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user=os.environ.get('DB_USER', 'root'), password=os.environ.get('DB_PASS', ''), host=os.environ.get('DB_HOST', 'localhost'), port=int(os.environ.get('DB_PORT', 26205)), connection_timeout=5, database=os.environ.get('DB_NAME', '1heartdb'), use_pure=True, charset='utf8')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Querytb1 where UserName='" + uname + "'")
    data1 = cur.fetchall()


    return render_template('UserQueryInfo.html', wait=data, answ=data1 )

@app.route("/AdminQinfo")
def AdminQinfo():

    #uname = session['uname']

    conn = mysql.connector.connect(user=os.environ.get('DB_USER', 'root'), password=os.environ.get('DB_PASS', ''), host=os.environ.get('DB_HOST', 'localhost'), port=int(os.environ.get('DB_PORT', 26205)), connection_timeout=5, database=os.environ.get('DB_NAME', '1heartdb'), use_pure=True, charset='utf8')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Querytb1")
    data = cur.fetchall()


    return render_template('AdminAnswer.html', data=data )







@app.route("/AdminAinfo")
def AdminAinfo():



    conn = mysql.connector.connect(user=os.environ.get('DB_USER', 'root'), password=os.environ.get('DB_PASS', ''), host=os.environ.get('DB_HOST', 'localhost'), port=int(os.environ.get('DB_PORT', 26205)), connection_timeout=5, database=os.environ.get('DB_NAME', '1heartdb'), use_pure=True, charset='utf8')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Querytb1 where  DResult !='waiting'")
    data = cur.fetchall()


    return render_template('AdminAnswer.html', data=data )




@app.route("/excelpost", methods=['GET', 'POST'])
def uploadassign():
    if request.method == 'POST':


        file = request.files['fileupload']
        import pandas as pd
        import matplotlib.pyplot as plt

        if not file or file.filename == '':
            return "No file selected! Please select a valid .csv dataset."

        file_extension = file.filename.rsplit('.', 1)[-1].lower()
        print("Detected file extension:", file_extension)

        if file_extension == 'xlsx':
            df = pd.read_excel(file, engine='openpyxl')
        elif file_extension == 'xls':
            df = pd.read_excel(file)
        elif file_extension == 'csv':
            df = pd.read_csv(file)
        else:
            return "Invalid file format! Please explicitly upload a .csv, .xls, or .xlsx file."
        
        # Ensure df is a DataFrame
        if not isinstance(df, pd.DataFrame) or df.empty:
            return "Failed to parse dataset into a valid DataFrame or dataset is empty."

        import seaborn as sns
        
        # Dynamically determine the target column for plotting (fallback to last column if named differently)
        target_column = 'HeartDisease' if 'HeartDisease' in df.columns else df.columns[-1]
        
        plt.figure(figsize=(8, 6))
        sns.countplot(x=target_column, data=df, label="Count")
        plt.title(f"Target Distribution: {target_column}")
        plt.savefig('static/images/out.jpg')
        plt.close()
        
        iimg = 'static/images/out.jpg'
        print("Feature Selection completed")

        import numpy as np
        from sklearn.model_selection import train_test_split
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.preprocessing import LabelEncoder
        from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
        import joblib
        import warnings
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        warnings.filterwarnings("ignore", category=FutureWarning)
        
        # Load the source of truth data intended for retraining framework
        data = pd.read_csv("heart_disease_with_troponin_angio.csv")  # Updated filename
        print(f"Retraining Model... Dataset Shape: {data.shape}")
        
        # Determine internal target column for system data
        sys_target = 'HeartDisease' if 'HeartDisease' in data.columns else data.columns[-1]
        
        plt.figure(figsize=(8, 6))
        sns.countplot(x=sys_target, data=data, label="Count")
        plt.title(f"Retraining Distribution: {sys_target}")
        plt.savefig('static/images/out2.jpg') # save so it doesn't wait for UI modal
        plt.close()

        # Label encode categorical columns
        categorical_cols = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope', 'HeartMRI', 'CTScan',
                            'Echocardiogram', 'ChestXray', 'Smoking']
        le = LabelEncoder()
        for col in categorical_cols:
            data[col] = le.fit_transform(data[col])

        # Features and target
        X = data.drop("HeartDisease", axis=1)
        y = data["HeartDisease"]

        # Clean NaNs and infinite values
        X.replace([np.inf, -np.inf], np.nan, inplace=True)
        X.dropna(inplace=True)
        y = y[X.index]  # Align target with features

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train model
        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        # Predict and evaluate
        y_pred = model.predict(X_test)
        print(f"Model Accuracy: {accuracy_score(y_test, y_pred):.2f}")
        print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
        print("\nClassification Report:\n", classification_report(y_test, y_pred))
        cm = confusion_matrix(y_test, y_pred)

        plt.figure(figsize=(6, 5))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=['No Disease', 'Disease'],
                    yticklabels=['No Disease', 'Disease'])
        plt.xlabel('Predicted Label')
        plt.ylabel('True Label')
        plt.title('Confusion Matrix')
        plt.show()

        # Save model
        joblib.dump(model, "heart_model.pkl")

        return render_template('ViewExcel.html', data=df.to_html(), dataimg=iimg)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
