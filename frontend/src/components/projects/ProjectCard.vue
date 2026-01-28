<script setup lang="ts">
defineProps<{
  id: number
  title: string
  coverUrl?: string | null
  updatedAt: string
  totalCost?: string | number
  participantsCount?: number
  updated_by_name?: string
}>()

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
    class="bg-dark-surface group cursor-pointer overflow-hidden rounded-xl border border-white/5 shadow-md transition-transform active:scale-[0.99]"
    @click="$emit('click')"
  >
    <!-- Картинка (если есть) -->
    <div v-if="coverUrl" class="relative h-40 w-full overflow-hidden">
      <img
        :src="coverUrl"
        alt="Cover"
        class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
      />
      <div
        class="from-dark-surface absolute inset-0 bg-gradient-to-t to-transparent opacity-60"
      ></div>
    </div>

    <!-- Заглушка, если картинки нет -->
    <div
      v-else
      class="bg-dark-surface flex h-24 items-center justify-center border-b border-white/5"
    >
      <span class="text-4xl">📁</span>
    </div>

    <!-- Контент -->
    <div class="p-4">
      <h3 class="text-dark-text mb-2 text-lg leading-tight font-bold">{{ title }}</h3>

      <!-- Цена (Акцент) -->
      <p v-if="totalCost" class="text-primary mb-3 font-semibold">
        {{ Number(totalCost).toLocaleString('ru-RU') }} ₽
      </p>

      <!-- Подвал карточки (Дата и люди) -->
      <div class="text-dark-muted mt-2 flex flex-col border-t border-white/5 pt-3 text-xs">
        <span>Обновлено: {{ formatDate(updatedAt) }}</span>
        <span>Кем обновлено: {{ updated_by_name }}</span>

        <!-- Индикатор участников -->
        <div v-if="participantsCount" class="flex items-center gap-1">
          👥 {{ participantsCount }}
        </div>
      </div>
    </div>
  </div>
</template>
