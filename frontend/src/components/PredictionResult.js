// PredictionResult.js
import React from 'react';
import { Line } from 'react-chartjs-2';
import '../styles/PredictionResult.css';

const PredictionResult = ({ data }) => {
  const { metrics, dates, demand } = data;

  // Prepare data for the chart
  const chartData = {
    labels: dates,
    datasets: [
      {
        label: 'Demanda',
        data: demand,
        borderColor: 'blue',
        fill: false,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    scales: {
      x: {
        title: { display: true, text: 'Fecha' },
      },
      y: {
        title: { display: true, text: 'Demanda (Cantidad)' },
      },
    },
  };

  return (
    <div className="prediction-result">
      <h3>Prediction Metrics</h3>
      <ul>
        <li><strong>Test MAE:</strong> {metrics.test_mae.toFixed(2)}</li>
        <li><strong>Test R²:</strong> {metrics.test_r2.toFixed(2)}</li>
        <li><strong>Test RMSE:</strong> {metrics.test_rmse.toFixed(2)}</li>
        <li><strong>Train R²:</strong> {metrics.train_r2.toFixed(2)}</li>
        <li><strong>Train RMSE:</strong> {metrics.train_rmse.toFixed(2)}</li>
      </ul>
      
      <h3>Demanda a lo largo del tiempo</h3>
      <div className="chart-container">
        <Line data={chartData} options={chartOptions} />
      </div>
    </div>
  );
};

export default PredictionResult;
