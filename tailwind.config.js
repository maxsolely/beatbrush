/** @type {import('tailwindcss').Config} */
module.exports = {
 purge: ['./pages/**/*.{js,ts,jsx,tsx}', './src/**/*.{js,ts,jsx,tsx}'],
 content: [
  './pages/**/*.{js,ts,jsx,tsx,mdx}',
  // Or if using `src` directory:
  './src/**/*.{js,ts,jsx,tsx,mdx}'
 ],
 theme: {
  extend: {}
 },
 plugins: []
};
