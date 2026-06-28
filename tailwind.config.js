/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.html",
    "./src/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#0B2046',
        background: '#F9F9F7',
        surface: '#FFFFFF',
        text: '#3A475C',
        muted: '#E2E6ED',
        accent: '#D4AF37',
      },
      fontFamily: {
        heading: ['Outfit', 'sans-serif'],
        body: ['"Plus Jakarta Sans"', 'sans-serif'],
      },
      fontSize: {
        'heading-lg': ['48px', { fontWeight: 600 }],
        'heading-md': ['32px', { fontWeight: 600 }],
        'heading-sm': ['24px', { fontWeight: 600 }],
        'body-base': ['16px', { fontWeight: 400 }],
        'label': ['13px', { fontWeight: 500, letterSpacing: '1px', textTransform: 'uppercase' }],
        'btn': ['15px', { fontWeight: 500 }],
      },
      borderRadius: {
        'sm': '8px',
        'md': '16px',
        'lg': '24px',
      },
      boxShadow: {
        'soft': '0 8px 32px rgba(11, 32, 70, 0.04)',
        'gold': '0 4px 24px rgba(212, 175, 55, 0.15)',
      },
    },
  },
  plugins: [],
}
