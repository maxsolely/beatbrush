module.exports = () => {
 const rewrites = () => {
  return [
   {
    source: '/api/:path*',
    destination:
     process.env.NODE_ENV === 'development'
      ? 'http://127.0.0.1:5001/api/:path*'
      : '/api/'
   }
  ];
 };
 return {
  rewrites
 };
};
