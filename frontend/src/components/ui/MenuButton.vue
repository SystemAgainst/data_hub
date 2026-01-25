<script setup lang="ts">
defineProps<{
  title: string
  subtitle?: string
  icon?: string // Можно передать имя иконки или эмодзи пока
  disabled?: boolean
}>()
</script>

<template>
  <button
    :disabled="disabled"
    class="w-full relative group overflow-hidden p-6 rounded-2xl text-left transition-all duration-300 border border-white/5 shadow-lg active:scale-[0.98]"
    :class="[
      disabled
        ? 'bg-dark-surface/50 opacity-60 cursor-not-allowed'
        : 'bg-dark-surface hover:bg-dark-surface/80 hover:border-primary/50',
    ]"
  >
    <!-- Градиентная подсветка при наведении (опционально для красоты) -->
    <div
      v-if="!disabled"
      class="absolute inset-0 bg-gradient-to-r from-primary/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"
    />

    <div class="relative flex items-center justify-between">
      <div>
        <h3 class="text-xl font-bold text-dark-text mb-1">{{ title }}</h3>
        <p v-if="subtitle" class="text-sm text-dark-muted">{{ subtitle }}</p>
      </div>

      <!-- Иконка/Стрелка -->
      <div
        class="text-2xl opacity-80 group-hover:opacity-100 group-hover:translate-x-1 transition-transform"
      >
        <slot name="icon">
          <!-- Стрелочка по дефолту -->
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="2"
            stroke="currentColor"
            class="size-6 text-primary"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3"
            />
          </svg>
        </slot>
      </div>
    </div>
  </button>
</template>
