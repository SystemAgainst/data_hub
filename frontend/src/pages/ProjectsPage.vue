<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useProjectsStore } from '@/stores/projects'
import ProjectCard from '@/components/projects/ProjectCard.vue'

const router = useRouter()

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
  router.push({ name: 'project-detail', params: { id } })
}
</script>

<template>
  <div class="flex h-full flex-col space-y-4">
    <!-- Шапка страницы -->
    <div class="flex items-center justify-between pb-2">
      <div>
        <nav class="text-dark-muted mb-1 flex items-center gap-1 text-xs">
          <span
            @click="$router.push('/')"
            class="hover:text-primary cursor-pointer transition-colors"
            >Главная</span
          >
          <span>/</span>
          <span class="text-white">Проекты</span>
        </nav>
        <h1 class="text-2xl font-bold">Отчетность</h1>
      </div>

      <button
        @click="$router.push('/')"
        class="bg-dark-surface flex h-10 w-10 items-center justify-center rounded-full border border-white/10 transition-all hover:bg-white/10 active:scale-95"
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
        class="bg-dark-surface text-dark-text focus:border-primary/50 w-full rounded-xl border border-white/10 py-3 pr-4 pl-10 shadow-sm transition-colors focus:outline-none"
      />
      <span class="text-dark-muted absolute top-3.5 left-3">🔍</span>
    </div>

    <!-- БЛОК КОНТЕНТА -->

    <!-- 1. Загрузка -->
    <div v-if="projectsStore.isLoading" class="text-primary animate-pulse py-10 text-center">
      Загрузка данных...
    </div>

    <!-- 2. Ошибка -->
    <div v-else-if="projectsStore.error" class="py-10 text-center text-red-400">
      {{ projectsStore.error }}
      <button
        @click="projectsStore.fetchProjects()"
        class="text-dark-muted mx-auto mt-2 block cursor-pointer text-sm underline"
      >
        Попробовать снова
      </button>
    </div>

    <!-- 3. Список (Если загрузилось и нет ошибок) -->
    <div v-else>
      <!-- Обертка для условия v-else -->

      <!-- Сами карточки -->
      <div v-if="filteredProjects.length > 0" class="grid gap-4 pb-10 sm:grid-cols-2">
        <ProjectCard
          v-for="project in filteredProjects"
          :key="project.id"
          :id="project.id"
          :title="project.title"
          :cover-url="project.cover_image"
          :updated-at="project.updated_at"
          :total-cost="project.total_cost"
          @click="openProject(project.id)"
          class="hover:border-primary cursor-pointer transition-all"
        />
      </div>

      <!-- Пустое состояние (Ничего не нашли) -->
      <div v-else class="text-dark-muted py-20 text-center">
        <div class="mb-2 text-4xl">🤔</div>
        <p>Ничего не найдено</p>
      </div>
    </div>
  </div>
</template>
