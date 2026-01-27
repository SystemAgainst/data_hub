<script setup lang="ts">
import AppWidget from '@/components/ui/AppWidget.vue'

defineProps<{
  stats: any // Можно описать строгий тип, но пока any
  isLoading: boolean
  sheetUrl?: string
}>()
</script>

<template>
  <AppWidget title="Сводка (Google Sheets)" icon="📊" :clickable="false" :external-link="sheetUrl">
    <!-- Скелетон загрузки -->
    <div v-if="isLoading" class="mt-2 animate-pulse space-y-3">
      <div class="h-6 w-1/2 rounded bg-white/10"></div>
      <div class="h-4 w-3/4 rounded bg-white/10"></div>
      <div class="h-4 w-full rounded bg-white/10"></div>
    </div>

    <!-- Данные -->
    <div v-else-if="stats" class="mt-2 space-y-4">
      <!-- ИТОГО -->
      <div class="flex items-end justify-between border-b border-white/5 pb-3">
        <div>
          <div class="text-dark-muted mb-1 text-xs">Всего потрачено</div>
          <div class="text-primary font-mono text-xl font-bold tracking-tight md:text-2xl">
            {{ stats.total_spent }} ₽
          </div>
        </div>
        <div class="text-right">
          <div class="text-dark-muted mb-1 text-xs">Дней</div>
          <div class="text-lg font-medium text-white">{{ stats.total_days }}</div>
        </div>
      </div>

      <!-- СПИСОК -->
      <div class="space-y-2">
        <div class="text-dark-muted text-xs">Расходы по участникам:</div>
        <div
          v-for="(p, index) in stats.participants"
          :key="index"
          class="group flex items-center justify-between text-sm"
        >
          <span class="text-gray-300 transition-colors group-hover:text-white">{{ p.name }}</span>
          <span class="group-hover:text-primary font-mono text-gray-400 transition-colors">{{
            p.amount
          }}</span>
        </div>
      </div>
    </div>

    <!-- Пусто -->
    <div v-else class="text-dark-muted py-6 text-center text-sm">Нет данных для отображения</div>
  </AppWidget>
</template>
