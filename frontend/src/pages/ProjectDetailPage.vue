<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getProjectById } from '@/api/projects'
import type { Project } from '@/types'

// Импорт компонентов (подставьте свои пути)
import ProjectHeader from '@/components/projects/detail/ProjectHeader.vue'
import ProjectInfoCard from '@/components/projects/detail/ProjectInfoCard.vue'
import ProjectTeamWidget from '@/components/projects/detail/ProjectTeamWidget.vue'
import ProjectDocumentsWidget from '@/components/projects/detail/ProjectDocumentsWidget.vue'

const route = useRoute()
const router = useRouter()

const project = ref<Project | null>(null)
const isLoading = ref(true)
const error = ref('')

const projectId = route.params.id as string

const fetchProject = async () => {
  try {
    isLoading.value = true
    error.value = ''
    // Приводим ID к числу, если api требует число, или оставляем строкой
    const { data } = await getProjectById(Number(projectId))
    project.value = data
  } catch (err: any) {
    console.error(err)
    error.value =
      err.response?.status === 404 ? 'Проект не найден' : 'Не удалось загрузить данные проекта'
  } finally {
    isLoading.value = false
  }
}

onMounted(fetchProject)
</script>

<template>
  <div class="mx-auto max-w-4xl pb-10">
    <!-- Навигация -->
    <button
      @click="router.back()"
      class="text-dark-muted mb-6 flex items-center gap-2 transition-colors hover:text-white"
    >
      ← Назад к списку
    </button>

    <!-- Состояния -->
    <div v-if="isLoading" class="text-dark-muted animate-pulse py-12 text-center">Загрузка...</div>

    <div v-else-if="error" class="rounded-2xl bg-red-500/10 p-6 text-center text-red-400">
      <p class="mb-4">{{ error }}</p>
      <button @click="router.push({ name: 'projects' })" class="text-white underline">
        На главную
      </button>
    </div>

    <!-- Основной контент -->
    <div v-else-if="project" class="space-y-6">
      <!-- 1. Шапка -->
      <ProjectHeader :project="project" @edit="console.log('Edit clicked')" />

      <!-- 2. Инфо-карточка -->
      <ProjectInfoCard :project="project" />

      <!-- 3. Виджеты (Сетка 2 колонки) -->
      <div class="mt-8 grid grid-cols-1 gap-4 md:grid-cols-2">
        <ProjectDocumentsWidget :has-documents="!!project.documents" />
        <ProjectTeamWidget :participants="project.participants_details" />
      </div>
    </div>
  </div>
</template>
