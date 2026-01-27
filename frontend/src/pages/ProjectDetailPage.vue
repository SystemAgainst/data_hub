<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getProjectById, getProjectStats } from '@/api/projects'
// ВАЖНО: Добавьте тип ProjectStats, если он экспортирован, иначе any
import type { Project, ProjectStats } from '@/types'

import ProjectHeader from '@/components/projects/detail/ProjectHeader.vue'
import ProjectInfoCard from '@/components/projects/detail/ProjectInfoCard.vue'
import ProjectTeamWidget from '@/components/projects/detail/ProjectTeamWidget.vue'
import ProjectDocumentsWidget from '@/components/projects/detail/ProjectDocumentsWidget.vue'
// 1. ИМПОРТИРУЕМ НОВЫЙ ВИДЖЕТ
import ProjectGoogleStatsWidget from '@/components/projects/detail/ProjectGoogleStatsWidget.vue'

const route = useRoute()
const router = useRouter()
const projectId = route.params.id as string

const project = ref<Project | null>(null)
const isLoading = ref(true)
const error = ref('')

// 2. ОБЪЯВЛЯЕМ СОСТОЯНИЕ ДЛЯ СТАТИСТИКИ
const stats = ref<ProjectStats | null>(null)
const isStatsLoading = ref(false)

const fetchStats = async () => {
  if (!project.value?.google_sheet_url) return

  isStatsLoading.value = true
  try {
    const { data } = await getProjectStats(projectId)
    stats.value = data
  } catch (e) {
    console.error('Ошибка загрузки статистики:', e)
  } finally {
    isStatsLoading.value = false
  }
}

const init = async () => {
  try {
    isLoading.value = true
    error.value = ''

    // Сначала грузим проект
    const { data } = await getProjectById(Number(projectId))
    project.value = data

    // 3. ЕСЛИ ЗАГРУЗИЛСЯ -> ГРУЗИМ СТАТИСТИКУ
    if (project.value) {
      // Не ждем (await) статистику, пусть грузится параллельно, чтобы не блочить UI
      fetchStats()
    }
  } catch (err: any) {
    console.error(err)
    error.value =
      err.response?.status === 404 ? 'Проект не найден' : 'Не удалось загрузить данные проекта'
  } finally {
    isLoading.value = false
  }
}

onMounted(init)
</script>

<template>
  <div class="mx-auto max-w-4xl pb-10">
    <!-- Навигация (всегда видна) -->
    <button
      @click="router.back()"
      class="text-dark-muted mb-6 flex items-center gap-2 transition-colors hover:text-white"
    >
      ← Назад к списку
    </button>

    <!-- 1. Состояние ЗАГРУЗКИ -->
    <div v-if="isLoading" class="text-dark-muted animate-pulse py-12 text-center">Загрузка...</div>

    <!-- 2. Состояние ОШИБКИ -->
    <div v-else-if="error" class="rounded-2xl bg-red-500/10 p-6 text-center text-red-400">
      <p class="mb-4">{{ error }}</p>
      <button @click="router.push({ name: 'projects' })" class="text-white underline">
        На главную
      </button>
    </div>

    <!-- 3. Состояние УСПЕХА (проект загружен) -->
    <div v-else-if="project" class="space-y-6">
      <ProjectHeader :project="project" @edit="console.log('Edit clicked')" />
      <ProjectInfoCard :project="project" />

      <div class="mt-8 grid grid-cols-1 gap-4 md:grid-cols-2">
        <!-- Виджет статистики -->
        <ProjectGoogleStatsWidget
          :stats="stats"
          :is-loading="isStatsLoading"
          :sheet-url="project.google_sheet_url"
        />

        <!-- Документы -->
        <ProjectDocumentsWidget :has-documents="!!project.documents" />

        <!-- Участники -->
        <ProjectTeamWidget :participants="project.participants_details" />
      </div>
    </div>
  </div>
</template>
