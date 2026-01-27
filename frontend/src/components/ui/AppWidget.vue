<script setup lang="ts">
defineProps<{
  title: string
  icon?: string // Эмодзи или имя иконки
  badge?: string | number // Число справа (например, кол-во людей)
  clickable?: boolean // Добавить ли ховер-эффекты
}>()
</script>

<template>
  <div
    class="bg-dark-surface flex h-full flex-col rounded-xl border border-white/5 p-4 transition-colors"
    :class="{ 'hover:border-primary/50 cursor-pointer': clickable }"
  >
    <!-- Шапка виджета -->
    <div class="mb-3 flex items-center justify-between">
      <div class="flex items-center gap-2">
        <span v-if="icon" class="text-2xl">{{ icon }}</span>
        <h4 class="font-medium text-white">{{ title }}</h4>
      </div>

      <!-- Бейдж (опционально) -->
      <span v-if="badge" class="text-dark-muted rounded-md bg-white/5 px-2 py-1 text-xs">
        {{ badge }}
      </span>
    </div>

    <!-- Слот для уникального контента -->
    <div class="flex-1">
      <slot />
    </div>
  </div>
</template>
