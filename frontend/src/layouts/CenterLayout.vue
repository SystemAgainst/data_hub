<template>
  <div class="min-h-screen flex flex-col items-center justify-center p-6 safe-pb">
    <!-- Логотип/Заголовок (опционально) -->
    <header class="mb-10 text-center">
      <h1 class="text-3xl font-bold tracking-tight text-primary">Data Hub</h1>
      <p class="text-dark-muted mt-2 text-sm">Информационная система ИП</p>
    </header>

    <!-- Контент (Форма или Кнопки) -->
    <main class="w-full max-w-sm space-y-6">
      <slot />
    </main>

    <!-- Копирайт или версия снизу -->
    <footer class="fixed bottom-6 text-xs text-dark-muted/50 safe-pb">v0.1.0 MVP</footer>
  </div>
</template>
