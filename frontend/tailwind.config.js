/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        obsidian: {
          950: '#070709',
          900: '#0A0A0C',
          850: '#0F0F13',
          800: '#121216',
          750: '#17171E',
          700: '#1C1D26',
        },
        emerald: {
          400: '#34D399',
          500: '#10B981',
          600: '#059669',
          glow: 'rgba(16, 185, 129, 0.25)'
        },
        indigo: {
          400: '#818CF8',
          500: '#6366F1',
          600: '#4F46E5',
          glow: 'rgba(99, 102, 241, 0.25)'
        }
      },
      fontFamily: {
        sans: ['"Plus Jakarta Sans"', 'Inter', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'monospace'],
        display: ['"Space Grotesk"', 'sans-serif'],
      },
      boxShadow: {
        'glow-emerald': '0 0 25px rgba(16, 185, 129, 0.2)',
        'glow-indigo': '0 0 25px rgba(99, 102, 241, 0.25)',
        'card-depth': '0 20px 40px -15px rgba(0, 0, 0, 0.7)',
        'elevated': '0 10px 30px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.08)',
      },
      animation: {
        'shimmer': 'shimmer 4s linear infinite',
        'pulse-subtle': 'pulseSubtle 3s ease-in-out infinite',
      },
      keyframes: {
        shimmer: {
          '0%': { backgroundPosition: '-200% 0' },
          '100%': { backgroundPosition: '200% 0' },
        },
        pulseSubtle: {
          '0%, 100%': { opacity: '1', transform: 'scale(1)' },
          '50%': { opacity: '0.85', transform: 'scale(1.02)' },
        }
      }
    },
  },
  plugins: [],
}
