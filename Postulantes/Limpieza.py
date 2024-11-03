from Forms import forms_to_sheets
import pandas as pd

def limpieza():
    data = forms_to_sheets()
    # Seleccionar las columnas necesarias (ajusta según tus necesidades)
    relevant_columns = [
        'Numero de empleados', 
        '¿Tu empresa está constituida en Cámara de Comercio?', '¿Desde hace cuánto inicio tu empresa?', '¿Darías un porcentaje de tu empresa para participar en el programa de Aceleracion?',
        'Cuánto es tu ingreso mensual recurrente (millones de pesos colombianos)', '¿A qué sector económico pertenece tu emprendimiento?',
        '¿Cuál es la tasa de crecimiento año o periodo?', '¿Cuál es tu margen bruto?', '¿Qué estás buscando actualmente?', 'MVP desarrollado',
        '¿Cuál es tu margen operacional?', '¿Qué tipo de clientes tienes actualmente?'
    ]
    data = data[relevant_columns]

    # Codificar columnas categóricas
    data['¿Tu empresa está constituida en Cámara de Comercio?'] = data['¿Tu empresa está constituida en Cámara de Comercio?'].apply(lambda x: 1 if x.lower() == 'sí' else 0)

    # Convertir rangos en 'Tasa de crecimiento' y otras variables a valores numéricos
    # Ajusta las conversiones de acuerdo a tu formato
    data['¿Cuál es la tasa de crecimiento año o periodo?'] = data['¿Cuál es la tasa de crecimiento año o periodo?'].replace({
        '5% a 10%': 7.5,
        '10% a 15%': 12.5,
        '15% a 20%': 17.5
    }).astype(float)
    data['Cuánto es tu ingreso mensual recurrente (millones de pesos colombianos)'] = data['Cuánto es tu ingreso mensual recurrente (millones de pesos colombianos)'].replace({
        'No tiene': 0,
        '0 a 10 millones': 5,
        '10 a 30 millones': 20,
        '30 a 50 millones': 40,
        '50 a 100 millones': 75,
        'Mas de 100 millones': 150
    }).astype(float)
    data['¿Qué tipo de clientes tienes actualmente?'] = data['¿Qué tipo de clientes tienes actualmente?'].replace({
        'B2c': 1,
        'B2b': 2,
        'B2b y B2c': 3,
        'B2b2c': 4,
        'Otros': 5
    }).astype(int)
    # Manejo de valores nulos (puedes elegir otra estrategia si prefieres)
    data.fillna(0, inplace=True)

    #Columnas cualitativas a cuantitativas
    data['¿A qué sector económico pertenece tu emprendimiento?'] = data['¿A qué sector económico pertenece tu emprendimiento?'].map({
        'Fintechh': 1, 'E-Commerce / Marketplace': 2, 'SaaS': 3, 'HealthTech': 4, 'AI': 5,
        'Eduación / Edtech': 6, 'Agricultura / AgroTech': 7, 'Industria': 8, 'Servicios Marketing / Digital Media': 9, 'Logistica/ Delivery': 10,
        'Retail / Retailtech': 11, 'Turismo / Traveltech': 12, 'PropTech': 13, 'Gaming': 14, 'Blockchain': 15, 'Robotica / Hardware': 16, 'BioTech': 17, 'Wellness': 18, 'Otro': 19
    })
    data['¿Tu empresa está constituida en Cámara de Comercio?'] = data['¿Tu empresa está constituida en Cámara de Comercio?'].map({
        'Sí': 1, 'No': 0})
    data['¿Desde hace cuánto inicio tu empresa?'] = data['¿Desde hace cuánto inicio tu empresa?'].map({'Aun no inicio': 0, 'Menos de 1 año': 1, 'Entre 1 y 3 años': 2, 'Mas de 3 años': 3})
    data['¿Darías un porcentaje de tu empresa para participar en el programa de Aceleracion?'] = data['¿Darías un porcentaje de tu empresa para participar en el programa de Aceleracion?'].map({'Si': 1, 'No': 0})
    data['¿Qué estás buscando actualmente?'] = data['¿Qué estás buscando actualmente?'].map({'Clientes': 1, 'Aliados': 2, 'Inversionistas': 3, 'Mercados internacionales': 4, 'otros': 5})
    data['MVP desarrollado'] = data['MVP desarrollado'].map({'SI': 1, 'NO': 0})
    # Aplicar ponderaciones
    # Definir ponderaciones (ajusta según tu criterio)
    weights = {
        'Numero de empleados': 0.05,
        '¿Tu empresa está constituida en Cámara de Comercio?': 0.1,
        '¿Desde hace cuánto inicio tu empresa?': 0.08,
        '¿Darías un porcentaje de tu empresa para participar en el programa de Aceleracion?': 0.07,
        'Cuánto es tu ingreso mensual recurrente (millones de pesos colombianos)': 0.2,
        '¿A qué sector económico pertenece tu emprendimiento?': 0.05,
        '¿Cuál es la tasa de crecimiento año o periodo?': 0.15,
        '¿Cuál es tu margen bruto?': 0.1,
        '¿Qué estás buscando actualmente?': 0.05,
        'MVP desarrollado': 0.1,
        '¿Cuál es tu margen operacional?': 0.03,
        '¿Qué tipo de clientes tienes actualmente?': 0.02
    }

    # Crear una columna ponderada
    data['Puntaje'] = data.apply(lambda row: sum(row[col] * weight for col, weight in weights.items()), axis=1)

    # Ver el DataFrame preprocesado
    print(data.head())
    return data