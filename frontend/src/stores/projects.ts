import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { Project } from '@/types'
import { getProjects } from '@/api/projects'

export const useProjectsStore = defineStore('projects', () => {
  const projects = ref<Project[]>([])
  const isLoading = ref(false)
  const error = ref<string | null>(null)

  const resetStore = () => {
    projects.value = []
    error.value = null
    isLoading.value = false
  }

  // Функция загрузки (Action)
  const fetchProjects = async () => {
    // Если уже загружали и прошло мало времени - можно не грузить (кеш),
    // но пока будем грузить всегда для актуальности.
    isLoading.value = true
    error.value = null

    try {
      const response = await getProjects()
      projects.value = response.data
    } catch (err) {
      console.error('Ошибка загрузки:', err)
      error.value = 'Не удалось загрузить проекты'
      // Важно: если ошибка, можно тоже очистить старые данные, чтобы не вводить в заблуждение
      projects.value = []
    } finally {
      isLoading.value = false
    }
  }

  return {
    projects,
    isLoading,
    error,
    fetchProjects,
    resetStore,
  }
})
