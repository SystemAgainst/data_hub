<script setup lang="ts">
// Описываем, какие данные принимает карточка
defineProps<{
  id: number
  title: string
  coverUrl?: string | null // Картинка может быть null
  updatedAt: string
  totalCost?: string | number // Пока опционально
  participantsCount?: number // Сколько людей в проекте
}>()

// Форматирование даты
const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    hour: '2-digit',
    minute: '2-digit',
  })
}
</script>

<template>
  <div
    class="bg-dark-surface rounded-xl overflow-hidden border border-white/5 shadow-md active:scale-[0.99] transition-transform cursor-pointer group"
    @click="$emit('click')"
  >
    <!-- Картинка (если есть) -->
    <div v-if="coverUrl" class="h-40 w-full overflow-hidden relative">
      <img
        :src="coverUrl"
        alt="Cover"
        class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
      />
      <div
        class="absolute inset-0 bg-gradient-to-t from-dark-surface to-transparent opacity-60"
      ></div>
    </div>

    <!-- Заглушка, если картинки нет -->
    <div
      v-else
      class="h-24 bg-dark-surface border-b border-white/5 flex items-center justify-center"
    >
      <span class="text-4xl">📁</span>
    </div>

    <!-- Контент -->
    <div class="p-4">
      <h3 class="text-lg font-bold text-dark-text leading-tight mb-2">{{ title }}</h3>

      <!-- Цена (Акцент) -->
      <p v-if="totalCost" class="text-primary font-semibold mb-3">
        {{ Number(totalCost).toLocaleString('ru-RU') }} ₽
      </p>

      <!-- Подвал карточки (Дата и люди) -->
      <div
        class="flex items-center justify-between text-xs text-dark-muted mt-2 border-t border-white/5 pt-3"
      >
        <span>Обновлено: {{ formatDate(updatedAt) }}</span>

        <!-- Индикатор участников -->
        <div v-if="participantsCount" class="flex items-center gap-1">
          👥 {{ participantsCount }}
        </div>
      </div>
    </div>
  </div>
</template>
