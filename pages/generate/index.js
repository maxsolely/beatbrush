import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Generate = () => {
 const [base64ImageString, setBase64ImageString] = useState(null);
 const generateImage = async () => {
  const { data } = await axios.get('/api/generate_image');
  console.log(data);
  setBase64ImageString(data.artifacts[0].base64);
 };

 useEffect(() => {
  generateImage();
 }, []);

 return (
  <div>
   <img src={`data:image/jpeg;base64,${base64ImageString}`} alt="My Image" />
  </div>
 );
};

export default Generate;
