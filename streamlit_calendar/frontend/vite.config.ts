import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  base: './',
  plugins: [react()],
  build: {
    outDir: 'build',
    assetsDir: 'assets',
    sourcemap: true,
  },
  server: {
    port: 3001,
  },
});
