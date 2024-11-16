// src/App.js
import React, { useState } from 'react';
import Header from './components/Header';
import UploadForm from './components/UploadForm';
import PredictionResult from './components/PredictionResult';
import './styles/App.css';

const App = () => {
  const [predictionData, setPredictionData] = useState(null);

  const handlePredictionResult = (data) => {
    setPredictionData(data);
  };

  return (
    <div className="App">
      <Header />
      <main>
        <section>
          <UploadForm onPrediction={handlePredictionResult} />
        </section>
        {predictionData && (
          <section>
            <h2>Prediction Results</h2>
            <PredictionResult data={predictionData} />
          </section>
        )}
      </main>
    </div>
  );
};

export default App;
