import axios from 'axios';

const API_URL = 'http://localhost:5000/api/upload_sales';  // Ensure this matches your backend port

export const uploadSalesFile = async (file) => {
  const formData = new FormData();
  formData.append('file', file);

  try {
    const response = await axios.post(API_URL, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    return response.data;  // Ensure you return response data here
  } catch (error) {
    console.error("Error uploading file:", error);
    return null;
  }
};
