from flask import Flask, render_template, request, redirect, url_for,session
import pandas as pd
import numpy as np
import pickle
from werkzeug.utils import secure_filename
import os
from flask import jsonify


#prep data
def prep_data(df):
    
    cat_df = pd.get_dummies(df[['OverTime']], drop_first=True)
    num_df = df[['Age','HourlyRate','DailyRate','MonthlyIncome','TotalWorkingYears','YearsAtCompany','NumCompaniesWorked','DistanceFromHome']]
    new_df = pd.concat([num_df,cat_df], axis=1)
    return new_df

#
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

UPLOAD_FOLDER = './templates'
ALLOWED_EXTENSIONS = set(['csv'])



## Initialize the app
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/home')
def analysis_page():
	# render a static template
    return render_template('home.html')

@app.route('/')
def index():
	# redirect to home
	return redirect(url_for('analysis_page'))

@app.route('/prediction', methods=['GET','POST'])
def prediction_page():
    if request.method == 'POST':
        #check if post request has the file type
        if 'file' not in request.files:
            return render_template('home.html', error='No File part',retJson ='No file part')
        file = request.files['file']
        # if user the did not select file
        if file.filename == '':
            return render_template ('home.html',error='No file Selected', retJson='No File Selected')
        #check for allowed extension
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # load the model from disk
            loaded_model = pickle.load(open('./random_forest_hr_model.sav', 'rb'))
            # read csv
            data = pd.read_csv(filename)
            prediction = loaded_model.predict_proba(prep_data(data))
            # get percentage proba
            retJson = []
            count = 0
            for prob in prediction:
                count+=1
                retJson.append("The probability of Employee Attrition with index {} : {} % ".format(count,prob[0] * 100))



            #retJson =jsonify({'retJson' :retJson})

            return render_template('home.html',error=None, retJson= retJson )
	# render a static template
    return render_template('home.html')

@app.route('/attrition', methods=['GET','POST'])
def single_prediction_page():
    if request.method == 'POST':
        Age = request.form['Age']
        HourlyRate = request.form['HourlyRate']
        OverTime = request.form['OverTime']
        DailyRate = request.form['DailyRate']
        MonthlyIncome = request.form['MonthlyIncome']
        TotalWorkingYears = request.form['TotalWorkingYears']
        YearsAtCompany = request.form['YearsAtCompany']
        NumCompaniesWorked = request.form['NumCompaniesWorked']
        DistanceFromHome = request.form['DistanceFromHome']

        if len(Age) <= 0 or len(HourlyRate) <= 0 or len(OverTime) <= 0 or len(DailyRate) <= 0 or len(MonthlyIncome)<= 0 or len(TotalWorkingYears) <= 0 or len(YearsAtCompany) <= 0 or len(NumCompaniesWorked) <= 0:
            return render_template('home.html', retJson= 'All filed is required to make prediction' )

        if OverTime == 'Yes':
            OverTime_Yes = 1
        else:
            OverTime_Yes = 0
        #create a pandas dataframe
        df = pd.DataFrame([{'Age': Age, 'HourlyRate': HourlyRate,'DailyRate':DailyRate, 'MonthlyIncome': MonthlyIncome, 
                  'TotalWorkingYears':TotalWorkingYears, 'YearsAtCompany': YearsAtCompany, 'NumCompaniesWorked':NumCompaniesWorked,
                   'DistanceFromHome':DistanceFromHome, 'OverTime_Yes': OverTime_Yes}])
        loaded_model = pickle.load(open('./random_forest_hr_model.sav', 'rb'))
        #print(df.head())
        
        #temp =  [ Age, HourlyRate, DailyRate, MonthlyIncome,TotalWorkingYears, YearsAtCompany, NumCompaniesWorked,DistanceFromHome, OverTime_Yes]
        #temp = np.reshape(1,-1)

        prediction = loaded_model.predict_proba(df)
    
        retJson = []
        for prob in prediction:
            retJson.append("The probability  is : {} % ".format(prob[0] * 100))
 
        return render_template('prob.html',error=None, retJson= retJson )
	# render a static template
    return render_template('home.html')



if __name__ =='__main__':
    app.run(debug=True)


