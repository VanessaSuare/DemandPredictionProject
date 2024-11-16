"""."""
import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Path for the static PRICES.csv file
prices_file_path = os.path.join('uploads', 'PRECIOS.csv')


def load_data(sales_file_path, prices_file_path):
    """..."""
    ventas = pd.read_csv(sales_file_path, delimiter=';')
    precios = pd.read_csv(
        prices_file_path, encoding='ISO-8859-1', delimiter=';'
        )
    precios = precios.rename(
        columns={'101,00': 'PRECIOP', '102,00': 'PRECIOU'}
        )
    precios['PRECIOP'] = precios['PRECIOP'].str.replace(',', '.').astype(float)
    precios['PRECIOU'] = precios['PRECIOU'].str.replace(',', '.').astype(float)
    ventas.columns = ventas.columns.str.upper()
    return ventas, precios


def clean_transform_data(ventas, precios):
    """..."""
    ventas_precios = pd.merge(
        ventas,
        precios,
        how='left',
        left_on='ITEM',
        right_on='ITEM'
        )
    data_limpia = ventas_precios.dropna(subset=['PRECIOP'])
    data_limpia = data_limpia.drop(
        columns=[
            'FECHA',
            'NOMBRE ESTABLECIMIENTO CLIENTE',
            'DOCUMENTO VENTAS',
            'NOMBRE ITEM_y',
            'LAPSO'])
    data_limpia = data_limpia.rename(
        columns={
            'CANTIDAD 1': 'CANTIDAD',
            'NOMBRE ITEM_x': 'NOMBRE ITEM'
            })
    data_limpia['CANTIDAD'] = pd.to_numeric(
        data_limpia[
            'CANTIDAD'
            ], errors='coerce')
    def calcular_precio_total(row):
        """..."""
        return row['PRECIOP'] * row['CANTIDAD'] if row['PRECIOP'] > 0 else row['PRECIOU'] * row['CANTIDAD']
    data_limpia['PRECIO TOTAL'] = data_limpia.apply(
        calcular_precio_total, axis=1
        )
    data_limpia['FECHA REAL'] = pd.to_datetime(
        data_limpia['FECHA REAL'], format='%d/%m/%Y', errors='coerce'
        )
    data_limpia['DIA_SEMANA'] = data_limpia['FECHA REAL'].dt.dayofweek
    data_limpia['MES'] = data_limpia['FECHA REAL'].dt.month
    data_limpia['TRIMESTRE'] = data_limpia['FECHA REAL'].dt.quarter
    data_limpia['AÑO'] = data_limpia['FECHA REAL'].dt.year
    data_limpia = data_limpia.drop(columns=['FECHA REAL'])

    le_cliente = LabelEncoder()
    le_item = LabelEncoder()
    data_limpia['NOMBRE CLIENTE'] = le_cliente.fit_transform(
        data_limpia['NOMBRE CLIENTE']
        )
    data_limpia['NOMBRE ITEM'] = le_item.fit_transform(
        data_limpia['NOMBRE ITEM']
        )
    data_limpia = data_limpia.drop(columns=['CANTIDAD'])
    return data_limpia
