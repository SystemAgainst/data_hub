<script setup lang="ts">
import { ref, computed } from 'vue'
import ProjectCard from '@/components/projects/ProjectCard.vue'

// --- МОКОВЫЕ ДАННЫЕ (Потом заменим на API) ---
const mockProjects = [
  {
    id: 1,
    title: 'Ремонт офиса на Ленина',
    cover_image:
      'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=800&q=80',
    total_cost: 1250000,
    updated_at: '2026-01-24T14:30:00',
    participants: [1, 2], // id участников
  },
  {
    id: 2,
    title: 'Закупка оборудования',
    cover_image: null,
    total_cost: 450000,
    updated_at: '2026-01-20T10:00:00',
    participants: [1],
  },
  {
    id: 3,
    title: 'Аренда склада (Северный)',
    cover_image:
      'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=800&q=80',
    total_cost: 80000,
    updated_at: '2025-12-28T09:15:00',
    participants: [],
  },
]

// Состояние поиска
const searchQuery = ref('')

// Фильтрация (Computed - пересчитывается сама)
const filteredProjects = computed(() => {
  if (!searchQuery.value) return mockProjects

  const query = searchQuery.value.toLowerCase()
  return mockProjects.filter((p) => p.title.toLowerCase().includes(query))
})

const openProject = (id: number) => {
  console.log('Открыть проект:', id)
  // router.push(`/projects/${id}`) // Сделаем позже
}
</script>

<template>
  <div class="flex flex-col h-full space-y-4">
    <!-- Шапка страницы -->
    <div class="flex items-center justify-between pb-2">
      <!-- Хлебные крошки и заголовок -->
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

      <!-- Кнопка Назад (Круглая) -->
      <button
        @click="$router.push('/')"
        class="w-10 h-10 flex items-center justify-center rounded-full bg-dark-surface border border-white/10 active:scale-95 transition-all hover:bg-white/10"
      >
        ✕
      </button>
    </div>

    <!-- Поиск -->
    <div class="relative">
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Поиск по названию..."
        class="w-full bg-dark-surface border border-white/10 rounded-xl py-3 pl-10 pr-4 text-dark-text focus:outline-none focus:border-primary/50 transition-colors shadow-sm"
      />
      <span class="absolute left-3 top-3.5 text-dark-muted">🔍</span>
    </div>

    <!-- Список (с прокруткой, если их много) -->
    <div class="grid gap-4 sm:grid-cols-2 pb-10">
      <ProjectCard
        v-for="project in filteredProjects"
        :key="project.id"
        :id="project.id"
        :title="project.title"
        :cover-url="project.cover_image"
        :updated-at="project.updated_at"
        :total-cost="project.total_cost"
        :participants-count="project.participants.length"
        @click="openProject(project.id)"
      />
    </div>

    <!-- Пустое состояние -->
    <div v-if="filteredProjects.length === 0" class="text-center py-20 text-dark-muted">
      <div class="text-4xl mb-2">🤔</div>
      <p>Ничего не найдено</p>
    </div>
  </div>
</template>
