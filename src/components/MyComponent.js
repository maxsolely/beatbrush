import React, { useState, useEffect } from 'react';

const MyComponent = () => {
 const [message, setMessage] = useState('');
 const [loading, setLoading] = useState(true);

 useEffect(() => {
  fetch('/api/hello')
   .then((res) => res.json())
   .then((data) => {
    setMessage(data.message);
    setLoading(false);
   });
 }, []);

 return (
  <div className="container">
   <p> {!loading ? message : 'Loading..'}</p>
  </div>
 );
};

export default MyComponent;
