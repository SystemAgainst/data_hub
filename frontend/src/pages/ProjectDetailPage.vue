<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getProjectById } from '@/api/projects'
import type { Project } from '@/types'

const route = useRoute()
const router = useRouter()

const project = ref<Project | null>(null)
const isLoading = ref(true)
const error = ref('')

const projectId = route.params.id as string

const fetchProject = async () => {
  try {
    isLoading.value = true
    const { data } = await getProjectById(projectId)
    project.value = data
  } catch (err: any) {
    console.error(err)
    if (err.response?.status === 404) {
      error.value = 'Проект не найден'
    } else {
      error.value = 'Ошибка загрузки проекта'
    }
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  fetchProject()
})
</script>

<template>
  <div class="mx-auto max-w-4xl">
    <!-- Кнопка Назад -->
    <button
      @click="router.back()"
      class="text-dark-muted mb-6 flex items-center gap-2 transition-colors hover:text-white"
    >
      ← Назад к списку
    </button>

    <!-- Загрузка -->
    <div v-if="isLoading" class="text-dark-muted py-12 text-center">Загрузка данных проекта...</div>

    <!-- Ошибка -->
    <div v-else-if="error" class="rounded-2xl bg-red-500/10 p-6 text-center text-red-400">
      {{ error }}
      <div class="mt-4">
        <button @click="router.push({ name: 'projects' })" class="text-white underline">
          Вернуться ко всем проектам
        </button>
      </div>
    </div>

    <!-- Контент проекта -->
    <div v-else-if="project" class="space-y-6">
      <!-- Заголовок и основные действия -->
      <div class="flex items-start justify-between">
        <div>
          <h1 class="mb-2 text-3xl font-bold text-white">{{ project.title }}</h1>
          <p v-if="project.address" class="text-dark-muted flex items-center gap-2">
            📍 {{ project.address }}
          </p>
        </div>
        <!-- Заготовка под кнопку редактирования -->
        <button
          class="rounded-lg bg-white/5 px-4 py-2 text-white transition-colors hover:bg-white/10"
        >
          Редактировать
        </button>
      </div>

      <!-- Основная инфо-карточка -->
      <div class="bg-dark-surface rounded-2xl border border-white/5 p-6 shadow-lg">
        <h3 class="mb-4 text-lg font-semibold text-white">Детали проекта</h3>

        <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
          <div>
            <span class="text-dark-muted mb-1 block text-xs">Описание</span>
            <p class="leading-relaxed text-white">
              {{ project.description || 'Описание отсутствует' }}
            </p>
          </div>

          <div class="space-y-4">
            <div>
              <span class="text-dark-muted mb-1 block text-xs">Сроки проведения</span>
              <div class="text-white">
                {{ project.start_date || '?' }} — {{ project.end_date || '...' }}
              </div>
            </div>

            <div v-if="project.budget">
              <span class="text-dark-muted mb-1 block text-xs">Бюджет</span>
              <div class="text-primary font-mono text-lg">{{ project.budget }} ₽</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Сюда можно добавить табы: Сметы, Документы, Участники и т.д. -->
      <div class="mt-8 grid grid-cols-1 gap-4 md:grid-cols-2">
        <!-- КАРТОЧКА: Сметы (оставляем как есть или дорабатываем позже) -->
        <div
          class="bg-dark-surface hover:border-primary/50 cursor-pointer rounded-xl border border-white/5 p-4 transition-colors"
        >
          <div class="mb-2 flex items-center gap-3">
            <span class="text-2xl">📄</span>
            <h4 class="font-medium text-white">Документы</h4>
          </div>
          <p class="text-dark-muted text-xs">
            {{ project.documents ? 'Есть прикрепленные файлы' : 'Нет документов' }}
          </p>
        </div>

        <!-- КАРТОЧКА: Участники (ДИНАМИЧЕСКАЯ) -->
        <div class="bg-dark-surface rounded-xl border border-white/5 p-4">
          <div class="mb-3 flex items-center justify-between">
            <div class="flex items-center gap-2">
              <span class="text-2xl">👥</span>
              <h4 class="font-medium text-white">Команда проекта</h4>
            </div>
            <span class="text-dark-muted rounded-md bg-white/5 px-2 py-1 text-xs">
              {{ project.participants_details?.length || 0 }} чел.
            </span>
          </div>

          <!-- Список участников -->
          <div
            v-if="project.participants_details && project.participants_details.length > 0"
            class="flex flex-wrap gap-2"
          >
            <div
              v-for="user in project.participants_details"
              :key="user.id"
              class="flex cursor-default items-center gap-2 rounded-lg bg-white/5 px-3 py-1.5 transition-colors hover:bg-white/10"
              :title="user.username"
            >
              <!-- Аватарка (заглушка с инициалом) -->
              <div
                class="bg-primary/20 text-primary flex h-6 w-6 items-center justify-center rounded-full text-xs font-bold"
              >
                {{ (user.first_name?.[0] || user.username[0]).toUpperCase() }}
              </div>

              <!-- Имя -->
              <span class="text-sm text-gray-200">
                {{ user.username }}
              </span>
            </div>
          </div>

          <!-- Если участников нет -->
          <div v-else class="text-dark-muted py-2 text-center text-sm">Участники не назначены</div>
        </div>
      </div>
    </div>
  </div>
</template>
