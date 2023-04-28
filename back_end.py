import pandas as pd
file = "./data_ai/Crop_recommendation.csv"

df = pd.read_csv(file)

crops = df.label.unique()


range_df = pd.DataFrame(columns=['crop', 'N' ,'P', 'K', 'pH', 'Moisture'])

for i, crop in enumerate(crops):
    select_rows = df.loc[df['label'] == crop]
    print(crop)
    print(select_rows)

    new_row = pd.DataFrame.from_dict({'crop': [crop],
                                      'N_min': min(select_rows['N']), 'N_max': (max(select_rows['N'])),
                                      'P_min': min(select_rows['P']), 'P_max': (max(select_rows['P'])),
                                      'K_min': min(select_rows['K']), 'K_max': (max(select_rows['K'])),
                                      'A_min': min(select_rows['ph']), 'A_max': (max(select_rows['ph']))
                                      })
    range_df = pd.concat([range_df, new_row])

range_df.reset_index(inplace=True, drop=True)

range_df.to_csv("./data_ai/soil_param_thresholds.csv")
