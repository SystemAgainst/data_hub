<template>
  <div class="min-h-screen bg-dark-bg safe-area flex flex-col">
    <!-- Просто слот для контента страницы -->
    <main class="flex-1 p-4">
      <div class="max-w-2xl mx-auto h-full flex flex-col">
        <slot />
      </div>
    </main>
  </div>
</template>

<style scoped>
.safe-area {
  padding-top: env(safe-area-inset-top);
  padding-bottom: env(safe-area-inset-bottom);
}
</style>
