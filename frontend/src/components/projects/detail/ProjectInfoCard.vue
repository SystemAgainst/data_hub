<script setup lang="ts">
import type { Project } from '@/types'

defineProps<{
  project: Project
}>()
</script>

<template>
  <div class="bg-dark-surface rounded-2xl border border-white/5 p-6 shadow-lg">
    <h3 class="mb-4 text-lg font-semibold text-white">Детали проекта</h3>

    <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
      <!-- Описание -->
      <div>
        <span class="text-dark-muted mb-1 block text-xs">Описание</span>
        <p class="leading-relaxed whitespace-pre-line text-white">
          {{ project.description || 'Описание отсутствует' }}
        </p>
      </div>
    </div>
  </div>
</template>
