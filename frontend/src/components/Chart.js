import React from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, LineElement, PointElement, LinearScale, Title, CategoryScale, Tooltip, Legend } from 'chart.js';
import '../styles/Chart.css';

// Register necessary components
ChartJS.register(LineElement, PointElement, LinearScale, CategoryScale, Title, Tooltip, Legend);

const Chart = ({ chartData }) => (
  <div className="chart-container">
    <h2>Demand Prediction Over Time</h2>
    <Line data={chartData} options={{ responsive: true }} />
  </div>
);

export default Chart;