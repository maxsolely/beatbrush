module.exports = () => {
 const rewrites = () => {
  return [
   {
    source: '/api/:path*',
    destination: 'http://127.0.0.1:5001/api/:path*'
   }
  ];
 };
 return {
  rewrites
 };
};
