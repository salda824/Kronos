from Limpieza import limpieza
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import numpy as np

data = limpieza()

historical_data = data[data['Estado'].notna()]  # Filtra los datos que ya tienen un estado definido
new_applicant = data[data['Estado'].isna()].iloc[-1:]  # Último registro sin estado

# Preparar los datos de entrenamiento
X_train = historical_data.drop(columns=['Estado'])
y_train = historical_data['Estado']

# Entrenamos al modelo
model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
model.fit(X_train, y_train)

# Predecir el estado del nuevo postulante
probs = model.predict_proba(new_applicant.drop(columns=['Estado']))
threshold = 0.7
predicted_class = "en revisión" if np.max(probs) < threshold else model.classes_[np.argmax(probs)]

# Actualizar el estado en el DataFrame y en Google Sheets
data.loc[new_applicant.index, 'Estado'] = predicted_class

# Actualizar el estado en Google Sheets
sheet.update_cell(new_applicant.index[0] + 2, data.columns.get_loc("Estado") + 1, predicted_class)  # +2 para ajustar el índice (fila de encabezado y base 1 en Sheets)

print(f"El nuevo postulante ha sido clasificado como: {predicted_class}")
