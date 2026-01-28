<script setup lang="ts">
import AppWidget from '@/components/ui/AppWidget.vue'

defineProps<{
  hasDocuments: boolean
}>()
</script>

<template>
  <AppWidget title="Документы" icon="📄" clickable>
    <div class="flex h-full flex-col items-start justify-center">
      <!-- Вариант: Явная кнопка для действия -->
      <a
        v-if="hasDocuments"
        href="https://disk.yandex.ru/client/disk/Недвижимость.%20Стройка.%20Торги/02_Объекты/пр-кт%20Находкинский%2C%2041"
        target="_blank"
        rel="noopener noreferrer"
        @click.stop
        class="group flex items-center gap-2 rounded-lg border border-blue-600/20 bg-blue-600/10 px-4 py-2 text-sm font-medium text-blue-500 transition-all hover:border-blue-600 hover:bg-blue-600 hover:text-white"
      >
        <span>Открыть на Диске</span>
        <!-- Иконка внешней ссылки (Visual cue) -->
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
          class="opacity-70 group-hover:opacity-100"
        >
          <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
          <polyline points="15 3 21 3 21 9"></polyline>
          <line x1="10" y1="14" x2="21" y2="3"></line>
        </svg>
      </a>

      <!-- Состояние Empty State -->
      <span v-else class="text-dark-muted flex items-center gap-2 text-xs opacity-50">
        <span class="block h-2 w-2 rounded-full bg-gray-500"></span>
        Документы отсутствуют
      </span>
    </div>
  </AppWidget>
</template>
