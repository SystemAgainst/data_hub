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
      class="rounded-lg bg-white/5 px-4 py-2 text-white transition-colors hover:bg-white/10"
    >
      Редактировать
    </button>
  </div>
</template>
