import pandas as pd
from flask import *
import pickle
import numpy as np



app = Flask(__name__)
model = pickle.load(open('data_ai/LogisticRegression.pkl', 'rb'))
param_thresholds = pd.read_csv('data_ai/soil_param_thresholds.csv')

def getCropRecommendation(N, P, K, A, T, M, R):
    data = np.array([[N, P, K, T, M, A, R]])
    prediction = model.predict(data)
    return prediction
#print(param_thresholds)

n_recco_reg = "Ammonium sulfate (21% N, 24% S); Urea (46% N); Diammonium phosphate/DAP (18% N; 44−46% P2O5)."
n_recco_org = "Manure – Rabbit, cow, horse, goat, sheep, and chicken manure; Compost/Vermi Compost added with: grass clippings, plant cuttings, and fruit and vegetable scraps"

p_recco_reg = "Diammonium phosphate/DAP (18% N; 44−46% P2O5); Monoammonium Phosphate/MAP (12% N; 61% P2O5)"
p_recco_org = "Compost/Vermi Compost added with: Eggs shells, banana peels, grains, and mushrooms."

k_recco_reg = "Muriate of Potash/Potassium Chloride; Potassium Sulphate (K 53%, S 17%); Monopotassium Phosphate (52% P, 34% K)"
k_recco_org = "Compost/Vermi Compost: Fruit and vegetable waste, Banana peels, but orange rinds, lemon rinds, beets, spinach, and tomatoes; Others: mined rock powders and wood ash"

a_increase = "lime-based compound such as dolomite lime and agricultural lime"
a_decrease = "Ammonium and sulfur fertilizers - Ammonium sulfate, ammonium nitrate, and urea"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        soil_parameters = request.form.to_dict(flat=False)
        print(type(soil_parameters['N'][0]))
        crop = getCropRecommendation(int(soil_parameters['N'][0]),
                                     int(soil_parameters['P'][0]),
                                     int(soil_parameters['K'][0]),
                                     int(soil_parameters['A'][0]),
                                     int(soil_parameters['T'][0]),
                                     int(soil_parameters['M'][0]),
                                     int(soil_parameters['R'][0]))
        print(crop[0])
        print(param_thresholds['crop'])
        param_ranges = param_thresholds.loc[param_thresholds['crop'] == crop[0]]
        param_ranges.reset_index(inplace=True)
        n_def = "No Deficiency"
        p_def = "No Deficiency"
        k_def = "No Deficiency"
        a_def = "Optimal pH"
        n_recco = "None"
        p_recco = "None"
        k_recco = "None"
        a_recco = "None"
        if int(soil_parameters['N'][0]) < param_ranges['N_max'][0]:
            n_def = "Nitrogen Deficiency"
            n_recco = "Regular Fertilizers: "+n_recco_reg+"\n"+"Organic Fertilizers: "+n_recco_org
        if int(soil_parameters['P'][0]) < param_ranges['P_max'][0]:
            p_def = "Phosphorous Deficiency"
            p_recco = "Regular Fertilizers: " + p_recco_reg + "\n" + "Organic Fertilizers: " + p_recco_org
        if int(soil_parameters['K'][0]) < param_ranges['K_min'][0]:
            k_def = "Potassium Deficiency"
            k_recco = "Regular Fertilizers: " + k_recco_reg + "\n" + "Organic Fertilizers: " + k_recco_org
        if int(soil_parameters['A'][0]) < param_ranges['A_min'][0]:
            a_def = "Lower pH"
            a_recco = a_increase
        if int(soil_parameters['A'][0]) > param_ranges['A_max'][0]:
            a_def = "Higher pH"
            a_recco = a_decrease
        return render_template("health_card.html", N=int(soil_parameters['N'][0]),
                               P=int(soil_parameters['P'][0]),
                               K=int(soil_parameters['K'][0]),
                               A=int(soil_parameters['A'][0]),
                               T=int(soil_parameters['T'][0]),
                               M=int(soil_parameters['M'][0]),
                               R=int(soil_parameters['R'][0]),
                               crop=crop[0],
                               n_def=n_def,
                               p_def=p_def,
                               k_def=k_def,
                               a_def=a_def,
                               n_recco = n_recco,
                               p_recco = p_recco,
                               k_recco = k_recco,
                               a_recco = a_recco)
    return render_template("recommender.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8787)
