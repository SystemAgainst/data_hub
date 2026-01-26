<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useProjectsStore } from '@/stores/projects'
import ProjectCard from '@/components/projects/ProjectCard.vue'

const projectsStore = useProjectsStore()
const searchQuery = ref('')

onMounted(() => {
  projectsStore.fetchProjects()
})

const filteredProjects = computed(() => {
  // Добавил проверку на undefined, чтобы не упало при первой загрузке
  const list = projectsStore.projects || []
  if (!searchQuery.value) return list

  const query = searchQuery.value.toLowerCase()
  return list.filter((p) => p.title.toLowerCase().includes(query))
})

const openProject = (id: number) => {
  console.log('Открыть:', id)
}
</script>

<template>
  <div class="flex flex-col h-full space-y-4">
    <!-- Шапка страницы -->
    <div class="flex items-center justify-between pb-2">
      <div>
        <nav class="text-xs text-dark-muted mb-1 flex items-center gap-1">
          <span
            @click="$router.push('/')"
            class="cursor-pointer hover:text-primary transition-colors"
            >Главная</span
          >
          <span>/</span>
          <span class="text-white">Проекты</span>
        </nav>
        <h1 class="text-2xl font-bold">Отчетность</h1>
      </div>

      <button
        @click="$router.push('/')"
        class="w-10 h-10 flex items-center justify-center rounded-full bg-dark-surface border border-white/10 active:scale-95 transition-all hover:bg-white/10"
      >
        ✕
      </button>
    </div>

    <!-- Поиск (Показываем всегда, кроме фатальной ошибки, чтобы не прыгал интерфейс) -->
    <div class="relative">
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Поиск по названию..."
        class="w-full bg-dark-surface border border-white/10 rounded-xl py-3 pl-10 pr-4 text-dark-text focus:outline-none focus:border-primary/50 transition-colors shadow-sm"
      />
      <span class="absolute left-3 top-3.5 text-dark-muted">🔍</span>
    </div>

    <!-- БЛОК КОНТЕНТА -->

    <!-- 1. Загрузка -->
    <div v-if="projectsStore.isLoading" class="py-10 text-center text-primary animate-pulse">
      Загрузка данных...
    </div>

    <!-- 2. Ошибка -->
    <div v-else-if="projectsStore.error" class="py-10 text-center text-red-400">
      {{ projectsStore.error }}
      <button
        @click="projectsStore.fetchProjects()"
        class="block mx-auto mt-2 text-sm underline text-dark-muted cursor-pointer"
      >
        Попробовать снова
      </button>
    </div>

    <!-- 3. Список (Если загрузилось и нет ошибок) -->
    <div v-else>
      <!-- Обертка для условия v-else -->

      <!-- Сами карточки -->
      <div v-if="filteredProjects.length > 0" class="grid gap-4 sm:grid-cols-2 pb-10">
        <ProjectCard
          v-for="project in filteredProjects"
          :key="project.id"
          :id="project.id"
          :title="project.title"
          :cover-url="project.cover_image"
          :updated-at="project.updated_at"
          :total-cost="project.total_cost"
          @click="openProject(project.id)"
        />
      </div>

      <!-- Пустое состояние (Ничего не нашли) -->
      <div v-else class="text-center py-20 text-dark-muted">
        <div class="text-4xl mb-2">🤔</div>
        <p>Ничего не найдено</p>
      </div>
    </div>
  </div>
</template>
