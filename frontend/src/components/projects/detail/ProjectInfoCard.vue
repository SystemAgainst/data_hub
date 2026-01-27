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

      <!-- Мета-данные -->
      <div class="space-y-4">
        <div>
          <span class="text-dark-muted mb-1 block text-xs">Сроки проведения</span>
          <div class="text-white">
            {{ project.created_at ? new Date(project.created_at).toLocaleDateString() : '?' }}
            <!-- (или используйте start_date/end_date если они есть в типе) -->
          </div>
        </div>

        <div v-if="project.total_cost">
          <span class="text-dark-muted mb-1 block text-xs">Бюджет</span>
          <div class="text-primary font-mono text-lg">{{ project.total_cost }} ₽</div>
        </div>
      </div>
    </div>
  </div>
</template>
