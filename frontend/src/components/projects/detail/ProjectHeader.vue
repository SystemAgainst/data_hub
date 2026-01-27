<script setup lang="ts">
import type { Project } from '@/types'

defineProps<{
  project: Project
}>()

defineEmits(['edit'])
</script>

<template>
  <div class="flex items-start justify-between">
    <div>
      <h1 class="mb-2 text-3xl font-bold text-white">{{ project.title }}</h1>
      <p v-if="project.address" class="text-dark-muted flex items-center gap-2">
        📍 {{ project.address }}
      </p>
    </div>
    <button
      @click="$emit('edit')"
      class="flex items-center justify-center rounded-lg bg-white/5 p-2 text-white transition-colors hover:bg-white/10 sm:px-4 sm:py-2"
      aria-label="Редактировать"
    >
      <!-- Иконка (видима всегда, или скрываем на desktop если хотите текст+иконка) -->
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="16"
        height="16"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
        class="sm:mr-2"
      >
        <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
        <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
      </svg>

      <!-- Текст (скрыт на мобильных 'hidden', виден от sm 'sm:inline') -->
      <span class="hidden text-sm font-medium sm:inline">Редактировать</span>
    </button>
  </div>
</template>
