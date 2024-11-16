import React, { useState } from 'react';
import { uploadSalesFile  } from '../services/api';
import Chart from '../components/Chart';
import '../styles/UploadForm.css';

const UploadForm = () => {
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState(null);
  const [chartData, setChartData] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return;
    const data = await uploadSalesFile(file);
    setResponse(data);

    // Prepare data for the chart
    if (data && data.predictions) {
      setChartData({
        labels: data.predictions.map((_, index) => `Prediction ${index + 1}`), // Label each prediction sequentially
        datasets: [
          {
            label: 'Predicted Demand',
            data: data.predictions,
            borderColor: 'rgba(75, 192, 192, 1)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            fill: true,
            tension: 0.1,
          },
        ],
      });
    }
  };

  return (
    <div>
      <h2>Upload Sales Data File</h2>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload and Predict</button>
      
      {response && (
        <div>
          <h3>Prediction Results</h3>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}

      {chartData && (
        <Chart chartData={chartData} />
      )}
    </div>
  );
};

export default UploadForm;
