import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import tailwindcss from '@tailwindcss/vite'
import { VitePWA } from 'vite-plugin-pwa'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
    tailwindcss(),
    VitePWA({
      registerType: 'autoUpdate',
      includeAssets: ['favicon.ico', 'apple-touch-icon.png', 'masked-icon.svg'],
      manifest: {
        name: 'Data Hub IP',
        short_name: 'DataHub',
        description: 'Информационная система для ИП',
        theme_color: '#1e293b', // Ваш темный фон
        background_color: '#1e293b',
        display: 'standalone', // Режим "как приложение"
        icons: [
          {
            src: 'pwa-192x192.png',
            sizes: '192x192',
            type: 'image/png',
          },
          {
            src: 'pwa-512x512.png',
            sizes: '512x512',
            type: 'image/png',
          },
        ],
      },
    }),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  server: {
    // Настройка Прокси: все запросы /api пойдут на Django
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000', // Адрес Django
        changeOrigin: true,
        secure: false,
      },
    },
  },
})
